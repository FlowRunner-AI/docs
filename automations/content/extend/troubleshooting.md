# Troubleshooting

Symptoms first, with the cause each one usually has.

## The deploy fails

**"Run `flowrunner login` first"** - there is no token in `.flowrunner/token`, or it was revoked by a
`logout`.

**"Session expired"** - the token was valid and is not any more. They last 30 days. Run `flowrunner login`
and deploy again.

**A `403` naming a mismatch** - the token belongs to a different workspace than `flowrunner.json` points at.
This is what you get after editing `workspaceId` by hand. Log in again instead.

**"Each service needs a `src/index.js`"** - the folder exists but nothing in it calls
`Flowrunner.createExtension`, or the module throws while loading. Check it builds first:

```js
// check-build.js, in the project root - run it, read it, delete it
const path = require('path')
const { getServiceDefinition } = require('./sandbox')

const definition = getServiceDefinition('tmdb', path.resolve('services/tmdb/src/index.js'))

for (const [name, method] of Object.entries(definition.methodsMap)) {
  console.log(method.registerAs.padEnd(20), name)
}
```

That prints every method the platform can invoke, and what kind each one is. A method missing from that list
is one no flow can reach.

**One service is skipped with a reason, the rest deploy** - by design. If *nothing* builds, the deploy
stops and reports every reason.

**"Invalid definition"** on a project that used to deploy - the CLI is older than the server expects.
Upgrade it in the project (`npm install -D flowrunner-cli@latest`) and deploy again.

**"Invalid definition: … sampleResultLoader Invalid input: expected object, received undefined"** on a
service copied from somewhere else - the folder holds a service in the legacy class-and-JSDoc format, which
the CLI does not deploy. Only `Flowrunner.createExtension` services deploy. Rewrite it, or ask the
[assistant](ai-assisted.md) to generate the same service in the current format from the old source.

**`FR_EXT_INVALID_SCHEMA`** - a `params`, `criteria` or `configItems` slot is not a `z.object`: a bare
`{ … }`, a single field, or a container wrapped in `.optional()`. Wrap it, and mark the *fields* optional.

**A load error naming `.labels()`** - the service uses the former `.map()` plugin, which no longer exists.
Move the API values into the `z.enum` list and the display names into `.labels()` - see
[Parameters & Types](parameters-and-types.md#showing-a-label-sending-a-value).

## The block does not appear in the editor

Reload the editor. An editor that was already open holds its block list until the page is reloaded.

If it is still missing, check the extension is listed under **Custom Extensions** with the version you
expect. A deploy that reported `same service` uploaded nothing, which is correct if the code has not
changed, and misleading if you expected it to have.

## The block errors immediately with "invalid params"

```
[flow-extension:tmdb] invalid params for method "discoverMovies" — minRating: «Minimum Rating» must be at most 10
```

A value failed a rule you declared, and the message names the field by its label. Every offending field is
listed, so read to the end. The usual causes:

- **A required field left blank** - `«Genre» is required`. Mark it `.optional()` or give it a `.default()`
  if the flow may legitimately leave it empty.
- **A value outside a limit or a format** - the message says what was expected.
- **A choice outside the list** - `«Sort By» must be one of: …`. Check `.labels()` maps display names to
  the values in the `z.enum`, not the other way round.

The same message with `invalid config` names a **configuration** value that no longer satisfies the schema -
typically a `.min()` or a new required field added in a redeploy. The extension's configuration form marks
the field when you open it - see [Service Structure](service-structure.md#what-the-workspace-fills-in) - so
fix it there and save.

If a service still declares `.nullish()` on fields the flow may leave blank, it keeps working. `.optional()`
is the ordinary form now that a blank is resolved by the declaration rather than by what the editor sent.

## A dropdown is empty

Your dictionary returned `{ items: [] }`. If that happened because the request failed rather than because
nothing matched, the flow builder has no way to tell. Check for a bare `try/catch` around the whole handler
and split it: unresolvable input is an empty list, a rejected credential is an error. See
[Dictionaries](dictionaries.md).

An empty dropdown on a **dependent** field usually means its `criteria` field is not filled in yet, which is
the intended behaviour.

## The extension cannot reach the API

**"MODULE_NOT_FOUND" on the first run after a deploy** - a dependency was installed at the project root
instead of inside the service folder. Only `services/<id>/node_modules` is packed:

```bash
cd services/tmdb && npm install the-package
```

**Every call is unauthorized** - the configuration is empty, or the key is being read from the wrong place.
Check the values on the extension's configuration tab, then run one method from its execute tab, which
confirms a key without building a flow around it. Both are shown in
[Write It Yourself](getting-started.md#fill-in-the-api-key).

**A parameter arrives at the API as `null`** - `.query()` serializes `null` as the string `null`. Strip
empty values before the call, on `undefined` and `null` rather than on falsiness, since `''`, `0` and
`false` are legitimate values.

**Two `?` in a URL** - an inline query string was combined with `.query()`. Pass a bare path and put every
parameter in `.query()`.

## The tests fail after upgrading the CLI

`init` never overwrites the harness it copied into `sandbox/`, so an upgraded CLI runs your suites through
the old harness. `runServiceMethod` now takes one `configs` bag where the old harness took `appConfigs` and
`sharedConfigs`; a suite that still passes `appConfigs` runs every method with an empty configuration. Copy
the current harness over yours and update the suites - see
[Testing](testing.md#upgrading-the-harness).

## A multipart upload arrives empty

The request was built with `.form(data)` and then `.send()`-ed. `.form()` only stages the body; a bare
`.send()` issues the request with no body at all, and the vendor answers as though no parameters were
passed. Await the request instead:

```js
await request.form(form)      // correct
request.form(form).send()     // one empty request, silently
```

## A trigger fires once and then never again

Usually a watermark reading a field the API can return out of order. If the feed's newest item carries a
date far in the future, the first poll stores that value and nothing is ever newer.

Look at what the API returns at the top of the feed, and clamp the query if it includes anything unreleased,
unpublished or scheduled. See [Triggers](triggers.md).

## A trigger never fires at all

- The first poll after configuration **emits nothing by design**. It records where the feed stands.
- Its polling interval is set on the block itself and starts at 600 seconds - see
  [Triggers](triggers.md#what-the-flow-builder-sees).
- A guard on a missing param means an unconfigured trigger returns nothing, which is correct, and looks
  identical to a broken one.

For a realtime trigger, check the webhook was registered: `subscribe` runs when the flow starts, so a flow
that was never started has no registration.

## Things that break other people's flows

Worth knowing before you cause one, because none of these produce an error at deploy time:

| Change | What happens |
|---|---|
| Renaming a service id | Deploys a *different* extension. The old one stays live under its old id. |
| Renaming an action, trigger or dictionary id | Flows using it break. Ids are frozen after the first deploy. |
| Renaming a `params` key | The saved value no longer maps to anything. |
| Making an optional param required | Every existing block that left it blank starts failing. |
| Changing the shape of `result` | Expressions bound to a removed field stop resolving. |
| Changing `webhookData`'s shape | Live realtime triggers cannot read what they persisted. |
| Deleting an extension | Every flow using its blocks is left referring to something that no longer exists. No undo, and no warning at deletion time. |

## Error codes

Some of these are raised while the CLI builds your definition, so you see them **in your terminal** at
`flowrunner deploy` or `npm test`, code and all:

| Code | Raised when |
|---|---|
| `FR_EXT_DUPLICATE_ITEM_ID` | Two registered items share an id. Ids are unique across all kinds. |
| `FR_EXT_INVALID_TRIGGER_CONFIG` | A polling trigger declared zero or several mechanisms, or declared `dedupe` or `watermark` without a `fetch`. |
| `FR_EXT_REALTIME_SETUP` | `setupRealtimeTriggers` declared twice, or missing `subscribe`/`unsubscribe`. |
| `FR_EXT_OAUTH_SETUP` | `setupOauth2` declared twice, or an OAuth method invoked without it. |
| `FR_EXT_NOT_REGISTERED` | The module loaded but registered no extension for that id. |
| `FR_EXT_INVALID_SCHEMA` | A `params`, `criteria` or `configItems` slot is not a `z.object`. |

The rest are raised while a block runs, and reach the flow as messages prefixed
`[flow-extension:<serviceId>]`:

| Code | Raised when |
|---|---|
| `FR_EXT_UNKNOWN_METHOD` | A method name matches no action, dictionary, trigger or loader. |
| `FR_EXT_MISSING_METHOD_PARAM` | A required wrapper param is absent. |
| `FR_EXT_INVALID_METHOD_INPUT` | The input failed its schema. |
| `FR_EXT_INVALID_CONFIG` | A saved configuration value fails the schema. Fix it on the Configuration tab. |
| `FR_EXT_INVALID_CRITERIA` | A dictionary's `criteria` failed its schema. |
| `FR_EXT_UNKNOWN_TRIGGER` | A dispatch referenced an unregistered trigger id. |
| `FR_EXT_SIGNATURE_VERIFICATION_FAILED` | An inbound webhook failed signature verification. |
| `FR_EXT_FEATURE_NOT_ENABLED` | A handler touched `oauth` or `files` without enabling it. |

The Test Monitor and the flow's error exit carry the **message**, so make the message itself say what went
wrong, and do not write flow logic that branches on a code.

## Getting more detail

- The **execute** tab on the extension's page runs one method with values you type, in isolation from any
  flow ([Write It Yourself](getting-started.md#fill-in-the-api-key)).
- Running a single block in the editor shows the input alongside the result or the error in the Test
  Monitor ([Actions](actions.md#trying-an-action-without-a-flow)).
- **`logger.debug()`** in your handler instead of `console.log`. Its output is attributed to your extension
  and appears on the flow's **Logs** tab.
- **A unit test** reproduces most failures faster than either, since it shows what your code actually sent.

## Related

- [Testing](testing.md) - reproducing a failure locally
- [Deploying & Managing](deploying.md) - versions, rollback and what is cached
- [The FlowRunner CLI](cli.md) - the commands and their errors
