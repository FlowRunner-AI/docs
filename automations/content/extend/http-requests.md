# HTTP Requests

`Flowrunner.Request` is the HTTP client the runtime provides. It resolves inside any handler with no
`require` and nothing in the service's `package.json`.

Most of the time you use it once, inside `apiRequest`, and every action goes through that.

## Nothing is sent until you await it

Every chainable method returns the same request instance, and the instance is thenable. Building the chain
sends nothing; `await` issues the request:

```js
await Flowrunner.Request.get(url)                     // sends
await Flowrunner.Request.post(url).set(headers)       // sends
```

**`.send(body?)` is the exception: it is terminal.** It issues the request immediately and returns a plain
promise, so nothing chains after it:

```js
await Flowrunner.Request.post(url).set(headers).send(body)   // correct - .send() last
Flowrunner.Request.post(url).send(body).set(headers)         // TypeError: .set is not a function
```

By default the promise resolves to the response body.

## The verbs

| Call | Takes a body |
|---|---|
| `Flowrunner.Request.get(url)` | no |
| `Flowrunner.Request.head(url)` | no |
| `Flowrunner.Request.options(url)` | no |
| `Flowrunner.Request.post(url, body?)` | yes |
| `Flowrunner.Request.put(url, body?)` | yes |
| `Flowrunner.Request.patch(url, body?)` | yes |
| `Flowrunner.Request.delete(url, body?)` | yes |
| `new Flowrunner.Request(url, method, body?)` | yes, with the verb as a value |

**Use the constructor form when the method arrives as an argument**, which is the normal case inside a
shared `apiRequest`:

```js
return new Flowrunner.Request(fullUrl, method, body).set(headers).query(query)
```

Do not write `Flowrunner.Request[method.toLowerCase()](url)`. An object lookup keyed by a variable resolves
inherited names, so a `method` of `constructor` returns a function rather than a request, and the failure is
confusing rather than obvious.

The optional second argument is the body, identical to `.send(body)` except that it leaves the chain open.

## Query parameters

`.query(obj)` appends to the query string:

```js
await Flowrunner.Request.get('https://api.vendor.com/items')
  .query({ str: 'abc', num: 123, bool: true, list: [1, 2, 3] })
// → /items?str=abc&num=123&bool=true&list=1&list=2&list=3
```

- **An array repeats the key.** There is no bracket or comma form.
- **`undefined` values are dropped; `null` is serialized as the string `null`**, which is almost never what
  an API wants. Strip empty values before calling `.query()`, and strip on `undefined`/`null` rather than on
  falsiness, because `''`, `0` and `false` are all legitimate.

```js
function prune(query) {
  return Object.fromEntries(
    Object.entries(query ?? {}).filter(([, value]) => value !== undefined && value !== null)
  )
}
```

!!! warning "Never combine an inline query string with `.query()`"
    The two are concatenated without normalizing the separator, so
    `Request.get('/p?a=1').query({ b: 2 })` puts **`/p?a=1?b=2`** on the wire - a second `?` instead of an
    `&`. Pass a bare path and put every parameter in `.query()`.

## Headers

`.set()` takes a name and a value, or an object, and may be called repeatedly:

```js
await Flowrunner.Request.get(url)
  .set('X-Api-Key', apiKey)
  .set({ Accept: 'application/json' })
```

`.type(contentType)` is shorthand for `Content-Type`, though one is set for you when the body is an object
(`application/json`) or a form (multipart with a generated boundary). `.basicAuth({ token })` and
`.authKey(key)` cover the two common auth schemes; anything else is an ordinary header.

## Bodies

An object body is serialized as JSON:

```js
await Flowrunner.Request.post(url).send({ name: 'Bob', tags: ['a', 'b'] })
await Flowrunner.Request.post(url).type('text/plain').send('raw text')
```

For a multipart upload, `.form(data)` sets a form-data body, built with
`Flowrunner.Request.FormData`:

```js
const form = new Flowrunner.Request.FormData()

form.append('title', 'Holiday photo')                 // text part
form.append('photo', buffer, {                        // binary part
  filename   : 'shot.png',
  contentType: 'image/png',
})

await request.form(form)
```

This is a Node-style streaming FormData, not the browser one: values may be a string, Buffer or Stream, and
a binary part takes its name and type from the third argument. Pass `contentType` explicitly - omitted, one
is derived from the filename and you inherit whatever that lookup returns.

!!! warning "Never follow `.form(data)` with `.send()`"
    `.form()` only stages the body; `.send()` is what issues the request, and a bare `.send()` issues it
    with **no body at all** - no `Content-Type`, no fields, `Content-Length: 0`. The vendor then answers as
    though no parameters were passed, which reads like a bug in your parameter mapping rather than in the
    transport.

    ```js
    await request.form(form)      // correct
    await request.send(form)      // also correct
    request.form(form).send()     // WRONG - one empty request, silently
    ```

## Reading the response

| Call | Effect |
|---|---|
| *(default)* | resolves to the response body |
| `.unwrapBody(false)` | resolves to `{ status, statusText, headers, body }` |
| `.setEncoding(enc)` | decodes the response body with this encoding. Omit it, or pass `null`, to keep the raw bytes |
| `.setTimeout(ms)` | a per-request client timeout |

Use `.unwrapBody(false)` when the status or a header carries meaning: a pagination cursor in a `Link`
header, a `Retry-After`, a `204` that has to be told apart from an empty body.

**A download needs no encoding at all.** The body arrives as a `Buffer`, and `setEncoding` is what turns it
into a string - so passing an encoding is what corrupts a binary response, not what enables it:

```js
const bytes = await Flowrunner.Request.get(fileUrl)          // already a Buffer
```

`.setTimeout(ms)` sets a per-request client timeout. It does not bound how long your handler runs.

## Failures

A non-2xx rejects with a `ResponseError`:

| Property | Value |
|---|---|
| `status` | the HTTP status |
| `headers` | the response headers |
| `body` | the parsed response body |
| `message` | **the response body when there is one**, so it is not always a string. Otherwise `Status Code <status> (<statusText>)`. |

Because `message` is the raw body for most JSON APIs, an unhandled failure surfaces as an unreadable
`[object Object]`. Turning that into something a flow builder can act on is the main reason `apiRequest`
exists:

```js
} catch (error) {
  const failure = new Error(`TMDB ${ error?.status ?? '?' }: ${ describeFailure(error) }`)

  failure.status = error?.status      // dictionaries need this to tell 404 from 401
  throw failure
}

function describeFailure(error) {
  const body = error?.body

  if (body && typeof body === 'object') {
    return body.status_message ?? JSON.stringify(body)
  }

  return typeof error?.message === 'string' ? error.message : 'request failed'
}
```

A transport failure - a dropped connection, DNS, a refused socket - rejects with **no `status` and no
`body`**. Cover both shapes in your tests.

## Mutual TLS

An API requiring a client certificate needs it on every call, so it belongs in `apiRequest`:

```js
apiRequest: async ({ url, method = 'get', body, query, context }) =>
  new Flowrunner.Request(`${ context.baseUrl }${ url }`, method, body)
    .cert({ cert: context.clientCert, key: context.clientKey })
    .query(query),
```

## Related

- [Service Structure](service-structure.md) - where `apiRequest` is declared and what it receives
- [Actions](actions.md) - returning the provider's response to the flow
- [Testing](testing.md) - asserting what your service actually sent
