# Testing

`npx flowrunner init` puts a test harness in your project. It runs your extension through the **real** runtime
with HTTP intercepted at the socket, so a test asserts what the pod would have sent - the URL, the headers,
the query, the body - and nothing leaves the process.

There is no live-API test here: checking against the real vendor means deploying and running a flow.

## What is in the project

```
jest.config.js               the runner
jest.setup.js                silences console output during a run
sandbox/
  index.js                   the five exports below
  service.js                 runServiceMethod, getServiceConfigItems, getServiceDefinition
  nock-mock.js               createNockMock - wire-level intercept plus a history of every call
  files-mock.js              createFilesSandbox
services/<id>/tests/<id>.test.js     you create this - init does not
```

```bash
npm test                              # every suite
npx jest services/tmdb/tests          # one extension
npx jest services/tmdb/tests -t 'discoverMovies'
```

The harness is **copied** into the project, not linked, so it is yours to edit, and `npx flowrunner init` never
overwrites it. An SDK that opens its own sockets rather than going through `http` is invisible to the mock;
add a shim for it in `nock-mock.js` - the harness is copied in precisely so you can.

!!! note "Create the tests folder yourself"
    `init` writes `sandbox/` and the jest config but does not create `services/<id>/tests/`, so `npm test`
    on a fresh project reports no tests found. Add the folder and your first suite by hand.

### Upgrading the harness

Because the harness is copied and never overwritten, upgrading the CLI does not upgrade it. After
`npm install -D flowrunner-cli@latest`, copy the current files over yours:

```bash
cp node_modules/flowrunner-cli/project-files/sandbox/*.js sandbox/
cp node_modules/flowrunner-cli/project-files/jest.*.js .
```

then re-apply any shim you added to `nock-mock.js`. The harness that shipped before 0.0.7 took `appConfigs`
and `sharedConfigs`; the current one takes a single `configs` bag, and a suite still passing `appConfigs`
runs every method with an empty configuration.

## The five exports

`runServiceMethod` loads the module, builds the definition and invokes one method per call, so a suite
holds no state between tests.

| Export | For |
|---|---|
| `runServiceMethod(data)` | run one method the way the platform invokes it |
| | `configs` for what the workspace filled in, `executionContext` for `{ accessToken }` on an OAuth extension, `createFiles` for a file backend |
| `createNockMock()` | intercept and record HTTP at the socket |
| `getServiceConfigItems(id, entryPoint)` | the published config descriptions |
| `getServiceDefinition(id, entryPoint)` | the built model - everything the platform can invoke |
| `createFilesSandbox()` | a file backend for extensions that use one |

`runServiceMethod` resolves the method in the built definition and assembles its input **by declared param
name**, exactly as the platform does:

```js
const result = await runServiceMethod({
  serviceId, serviceEntryPointPath,
  configs   : { apiKey: 'test-api-key' },   // what the workspace filled in
  methodName: 'getMovieDetails',
  methodData: { movieId: '693134' },        // keyed by PARAM NAME
})
```

Because it maps by name, a suite catches a param whose declared name disagrees with what the handler reads:
the value arrives `undefined` rather than arriving in the wrong slot. A method name that is not in the
definition throws, listing the ones that are, since a method the platform cannot invoke is one no
flow can reach.

## The HTTP mock

Because the intercept is at the socket rather than around a client, a bundled SDK's requests are recorded
exactly as `Flowrunner.Request` ones are.

```js
let httpMock

beforeAll(() => { httpMock = createNockMock() })
afterEach(() => { httpMock.reset() })     // drops recorded calls and handlers
afterAll(() => { httpMock.dispose() })    // un-patches http - see below
```

```js
httpMock.onGet(url).reply({ items: [] })                       // 200 plus body
httpMock.onPost(url).reply(body, 201, headers)                 // explicit status and headers
httpMock.onPut · onPatch · onDelete · onHead · onOptions       // the other verbs
httpMock.on('propfind', url).reply(xml)                        // anything else
httpMock.onGet(url).replyWith(call => ({ … }))                 // dynamic, receives the history record
httpMock.onPost(url).replyWithError({ message: 'Nope' }, 422)  // an error RESPONSE
httpMock.onGet(url).replyWithNetworkError('ECONNRESET')        // a TRANSPORT failure
```

Handlers match in registration order, first one wins. A URL registered without a query string matches
whatever query your code added; one registered with a query string matches only that exact query.

!!! warning "`dispose()` is not optional"
    nock patches the shared `http` module when it activates, and jest gives every test file its own copy of
    nock but one `http`. A suite that skips `dispose()` leaves its activation stacked for the rest of the
    worker, and the layers corrupt each other - request bodies vanishing from `history`, errors with empty
    stacks. The damage lands on whichever suite runs **next**, which is why the symptom is "passes alone,
    fails in a full run".

### The history record

```js
expect(httpMock.history).toEqual([{
  method       : 'get',
  url          : `${ BASE }/movie/693134`,
  canonicalUrl : `${ BASE }/movie/693134`,    // scheme, host and path
  fullUrl      : `${ BASE }/movie/693134?api_key=test-api-key`,
  headers      : { … },
  query        : { api_key: 'test-api-key' },
  body         : undefined,
  formData     : undefined,
  contentType  : undefined,
  contentLength: 0,
  timeout      : undefined,
}])
```

Compare the whole record on the first test of each method: that is what catches the field you did not know
your extension was sending. Later tests in the same group can assert one field.

Three things the wire flattens, all of them assertion traps:

- **`query` values are re-typed by shape**, because a query string carries no types. `?limit=100&flag=true`
  reads back as `{ limit: 100, flag: true }`, and an id sent as the string `'123'` reads back as `123`.
  Assert the coerced value.
- **Header names come back in conventional casing.** The client lowercases them on the way out and the mock
  re-derives them, so `X-API-KEY` reads back as `X-Api-Key`.
- **`contentLength` is not guessable.** Write the assertion, run it, and take the real number from the diff.

For a multipart request the mock parses the parts into `formData` and leaves `body` undefined:

```js
formData: { _fields: [
  { name: 'title', value: 'Holiday photo',                    filename: undefined,  contentType: undefined },
  { name: 'photo', value: Buffer.from([0x89, 0x50, 0x4e, 0x47]), filename: 'shot.png', contentType: 'image/png' },
] }
```

Text parts arrive as strings, numbers included; binary parts as byte-exact Buffers carrying the filename and
content type you passed. Assert the bytes literally rather than a length, and match `contentType` with
`expect.stringMatching(...)` because the boundary is random per request. **An empty `_fields` array** is the
assertion that catches a request built with `.form(data)` and then `.send()`-ed, which goes out with no body
at all.

## How a suite is laid out

```js
'use strict'

const { createNockMock, getServiceConfigItems, runServiceMethod } = require('../../../sandbox')

const API_KEY = 'test-api-key'
const BASE    = 'https://api.themoviedb.org/3'

describe('TMDB Service', () => {
  const serviceId             = 'tmdb'
  const serviceEntryPointPath = require.resolve('../src/index.js')
  const configs               = { apiKey: API_KEY, language: 'en-US' }

  let httpMock

  function runMethod({ methodName, methodData, data }) {
    return runServiceMethod({ serviceId, serviceEntryPointPath, configs, ...data, methodName, methodData })
  }

  beforeAll(() => { httpMock = createNockMock() })
  afterEach(() => { httpMock.reset() })
  afterAll(() => { httpMock.dispose() })

  it('service config items', () => {
    expect(getServiceConfigItems(serviceId, serviceEntryPointPath)).toEqual([
      {
        name: 'apiKey', label: 'API Key', type: 'string',
        required: true, shared: false, options: [],
        description: 'Your TMDB v3 API key, from Settings -> API',
      },
      …
    ])
  })

  describe('Actions', () => {
    describe('discoverMovies', () => {
      function runDiscoverMoviesMethod(methodData, data) {
        return runMethod({ methodName: 'discoverMovies', methodData, data })
      }

      it('sends the genre and the default sort, and hands back the page whole', async () => {
        const page = { page: 1, total_pages: 3, results: [{ id: 693134, title: 'Dune: Part Two' }] }

        httpMock.onGet(`${ BASE }/discover/movie`).reply(page)

        await expect(runDiscoverMoviesMethod({ genreId: '878' })).resolves.toEqual(page)

        expect(httpMock.history[0].query).toEqual({
          with_genres: 878, sort_by: 'popularity.desc', api_key: API_KEY, language: 'en-US',
        })
      })

      it('reads the key from config rather than a hardcoded one', async () => {
        httpMock.onGet(`${ BASE }/discover/movie`).reply({ results: [] })

        await runDiscoverMoviesMethod({ genreId: '878' }, { configs: { apiKey: 'other-key' } })

        expect(httpMock.history[0].query.api_key).toBe('other-key')
      })

      it('rejects with the message the API sent when the key is refused', async () => {
        httpMock.onGet(`${ BASE }/discover/movie`)
          .replyWithError({ status_code: 7, status_message: 'Invalid API key.' }, 401)

        await expect(runDiscoverMoviesMethod({ genreId: '878' })).rejects.toThrow('TMDB 401: Invalid API key.')
      })

      it('rejects when the connection drops', async () => {
        httpMock.onGet(`${ BASE }/discover/movie`).replyWithNetworkError('ECONNRESET')

        await expect(runDiscoverMoviesMethod({ genreId: '878' })).rejects.toThrow()
      })
    })
  })
})
```

The nesting is fixed: the extension, then the group, then the method, then the tests. Groups come from what
a thing **is**, never from subject matter, and there are seven: `Actions`, `Dictionaries`,
`Polling Triggers`, `RealTime Triggers`, `DynamicResults`, `DynamicParams` and `OAuth`.

**Test both failure kinds.** An error response reaches your code as a `ResponseError` carrying `status` and
`body`; a dropped connection has neither. The `TMDB 401: …` message the third test expects is built by the
`apiRequest` on [HTTP Requests](http-requests.md#failures); the service as written in the code quick start has no
error handling yet, so that assertion holds only once that `apiRequest` is in place.

**Pass a different `configs` and assert what went on the wire.** That is how you prove a credential is
read from configuration and not hardcoded.

**Send the blanks the editor sends.** The flow editor delivers every untouched field as an explicit `null`,
so a test that passes `{ genreId: '878', year: null, sortBy: null }` and asserts the query proves that your
optional fields and defaults behave when a flow builder leaves them alone.

## Testing a dictionary

A dictionary takes `{ search, cursor, criteria }` wrapped in a single `payload`. Cover the mapping, a
case-insensitive search, and then the two cases that look alike and are not:

```js
describe('Dictionaries', () => {
  function runDictionaryMethod(methodName, payload) {
    return runMethod({ methodName, methodData: { payload } })
  }

  const runGetGenresDictionaryMethod  = (payload) => runDictionaryMethod('getGenresDictionary', payload)
  const runGetSeasonsDictionaryMethod = (payload) => runDictionaryMethod('getSeasonsDictionary', payload)

  it('filters on the typed text without regard to case', async () => {
    httpMock.onGet(`${ BASE }/genre/movie/list`).reply(GENRES)

    await expect(runGetGenresDictionaryMethod({ search: 'SCIENCE' })).resolves.toEqual({
      items : [{ label: 'Science Fiction', value: '878' }],
      cursor: null,
    })
  })

  it('answers an unmatched search with an empty list', async () => {
    httpMock.onGet(`${ BASE }/tv/999999`).replyWithError({ status_message: 'Not found.' }, 404)

    await expect(runGetSeasonsDictionaryMethod({ criteria: { tvId: '999999' } }))
      .resolves.toEqual({ items: [], cursor: null })
  })

  it('does not answer a rejected key with an empty list', async () => {
    httpMock.onGet(`${ BASE }/tv/95396`).replyWithError({ status_message: 'Invalid API key.' }, 401)

    await expect(runGetSeasonsDictionaryMethod({ criteria: { tvId: '95396' } })).rejects.toThrow()
  })
})
```

If the second fails because your dictionary swallows the error, that is a finding to fix in the extension,
not a test to rewrite into agreement with it.

## Testing a polling trigger

`runServiceMethod` can only invoke what the built definition exposes, and a trigger's `fetch` is not in it.
The platform reaches `fetch` through a SYSTEM method, and so does the harness - which matters, because the
mapping in between is the part most likely to be wrong. The payload goes one level down, under `invocation`:

```js
describe('Polling Triggers', () => {
  const SEEDED_PAGE = [{ id: 2, release_date: '2024-03-01' }, { id: 1, release_date: '2024-02-01' }]
  const NEW_RELEASE = { id: 3, release_date: '2024-04-01' }

  function runHandleTriggerPollingForEventMethod(invocation) {
    return runMethod({ methodName: 'handleTriggerPollingForEvent', methodData: { invocation } })
  }

  describe('onMovieReleased', () => {
    it('emits nothing on the first poll, and remembers where it got to', async () => {
      httpMock.onGet(`${ BASE }/discover/movie`).reply({ results: SEEDED_PAGE })

      const result = await runHandleTriggerPollingForEventMethod({
        eventName: 'onMovieReleased', triggerData: { genreId: '878' }, state: null,
      })

      expect(result.events).toEqual([])
    })

    it('emits only the releases past the remembered marker', async () => {
      const seeded = await runHandleTriggerPollingForEventMethod({
        eventName: 'onMovieReleased', triggerData: { genreId: '878' }, state: null,
      })

      httpMock.reset()
      httpMock.onGet(`${ BASE }/discover/movie`).reply({ results: [NEW_RELEASE, ...SEEDED_PAGE] })

      const result = await runHandleTriggerPollingForEventMethod({
        eventName: 'onMovieReleased', triggerData: { genreId: '878' }, state: seeded.state,
      })

      expect(result.events).toEqual([NEW_RELEASE])
    })
  })
})
```

Group by trigger, never by SYSTEM method. The groups are the things a flow builder picks from a list.

Polling is about state, so the pair above - the seeding poll emits nothing, the next emits only what is new
- is the minimum worth having. A third test that pins the query is what catches a watermark reading a field
the API can hand back out of order.

## What not to do

| | Why |
|---|---|
| `require()` the entry file, or touch `global.Flowrunner` | Behaviour unreachable through a method call is not your extension's contract |
| `jest.mock` a transport, or hand-write a fake client | The socket-level mock records what your code *sent*; a fake records what you expected it to send |
| `it.each`, or `expect` inside a loop | N results collapse into one unreadable failure |
| A catch-all handler | Every method under test calls a known URL; a catch-all only hides a wrong one |
| Test that the vendor's API returns correct data | That is what deploying and running a flow is for |
| Change the extension to make a test pass | A green test asserting a bug reads as "this is correct" |

## Related

- [Actions](actions.md) - what a handler receives and returns
- [Dictionaries](dictionaries.md) - the empty-list rule these tests pin
- [Triggers](triggers.md) - the SYSTEM methods a trigger is driven through
- [HTTP Requests](http-requests.md) - what the mock is recording

<!-- 2026-09-22 (FR-3627): the `TMDB 401: ...` assertion now points at the apiRequest on http-requests.md
     that produces the message; the getting-started.md version of the service has no error handling.
     Commands switched to `npx flowrunner` - see the drive record on cli.md. -->
