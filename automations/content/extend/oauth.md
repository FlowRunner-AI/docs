# OAuth2

Some APIs authenticate with an API key, which is a config item and nothing more. Others need each workspace
to connect its own account, and that is OAuth. Declare it once with `ext.setupOauth2()`, and its presence
alone is what tells FlowRunner your extension needs a connection.

```js
ext.setupOauth2({
  scopes      : ['boards:read', 'notes:write'],
  authorizeUrl: 'https://api.notes.example/oauth/authorize',
  tokenUrl    : 'https://api.notes.example/oauth/token',
  clientAuth  : 'basic',

  identityRequest: ({ apiRequest }) => apiRequest({ url: '/me' }),
  identity       : (raw) => ({ name: raw.display_name, imageUrl: raw.avatar_url }),
})
```

For the common case that is the whole declaration: the runtime drives the authorize redirect, the token
exchange and the refresh.

## Where the client id and secret go

**In ordinary `configItems`, as per-app fields.**

```js
configItems: z.object({
  clientId    : z.string().label('Client ID').describe('From your app in the provider console'),
  clientSecret: z.string().secret().label('Client Secret'),
}),
```

Whoever administers the workspace registers an application with the provider, then pastes the two values
into the extension's configuration, the same as any other config item - see
[Service Structure](service-structure.md#what-the-workspace-fills-in).

Mark the secret `.secret()` so the configuration form masks it. `.shared()`, which the platform's own
extensions use to fill client credentials in once for every workspace, does nothing in a custom extension:
there is a single configuration form, every field is on it, and the value reaches `config` either way.
Leave it off.

## What you declare

| Property | Type | What it does |
|---|---|---|
| `scopes` | string[] | The base scope list. |
| `authorizeUrl` / `tokenUrl` | string | The provider's endpoints. |
| `pkce` | boolean | The runtime generates the verifier and challenge and threads the state. |
| `clientAuth` | `'basic'` or `'body'` | Where the client credentials are placed on the token request. |
| `identityRequest` | function | `({ apiRequest }) => raw` - fetches the connected account. |
| `identity` | function | `(raw) => ({ name, imageUrl?, userData? })` - what the console shows. |
| `serializeToken` / `deserializeToken` | function | For providers whose token is more than one value. |
| `getConnectionURL` | function | Escape hatch: build the authorize URL yourself. |
| `executeCallback` | function | Escape hatch: handle the callback yourself. |
| `refreshToken` | function | Escape hatch: refresh the token yourself. |

`identity` is worth filling in. It is what turns a connection in the console from an anonymous entry into
the account it actually belongs to, which matters as soon as a workspace has two.

## Using the token

The access token reaches every handler on `oauth`:

```js
apiRequest: async ({ url, method = 'get', body, query, context, oauth }) => {
  return new Flowrunner.Request(`${ context.baseUrl }${ url }`, method, body)
    .set({ Authorization: `Bearer ${ oauth.accessToken }` })
    .query(query)
},
```

Put it in `apiRequest` rather than in each action, the same as any other credential.

!!! note "`oauth` is empty before a connection exists"
    `initContext` also runs during the OAuth flow itself, when there is no token yet. Read `oauth` with
    `oauth?.accessToken` there rather than assuming it is present, or connecting will fail on the first
    step.

## Scopes

The authorize URL asks for the union of the extension's `scopes` and the `oauth2Scopes` declared on
individual items, deduplicated. That lets a rarely-used action ask for a permission the rest of the
extension does not need:

```js
ext.addAction({
  id          : 'deleteNote',
  oauth2Scopes: ['notes:delete'],
  …
})
```

!!! warning "Scopes on a realtime trigger are not collected"
    The union covers actions, polling triggers and dictionaries. Scopes declared on a **realtime** trigger
    are currently not added to the authorize URL, so a connection made without them will be refused when the
    trigger tries to subscribe. Put a realtime trigger's scopes in the extension-level `scopes` instead.

## Tokens that are more than a string

Some providers hand back a token plus something you need alongside it - an instance URL, a tenant id, an
account identifier. `serializeToken` and `deserializeToken` let you store the pair and read it back:

```js
serializeToken  : (token) => JSON.stringify({ access: token.access, instance: token.instance_url }),
deserializeToken: (raw) => JSON.parse(raw),
```

The deserialized value arrives as `oauth.token`. It is the one part of the handler bag that is not typed
from your declarations, because `setupOauth2` runs after the service's shape is resolved, so annotate it
where you read it if the shape matters.

## When the declarative form is not enough

Three escape hatches replace one step each, and leave the rest alone:

| Handler | Receives | Returns |
|---|---|---|
| `getConnectionURL` | `{ config, context, scopes }` | the authorize URL |
| `executeCallback` | `{ callbackObject, config, context }` | `{ token, expirationInSeconds?, refreshToken?, … }` |
| `refreshToken` | `{ refreshToken, config, context }` | `{ token, expirationInSeconds?, refreshToken? }` |

Reach for them when a provider deviates from the standard flow: a non-standard parameter on the authorize
URL, a token response that has to be unwrapped, a refresh that is a different endpoint entirely.

## When a connection will not work

| Symptom | Usual cause |
|---|---|
| The connection fails immediately, no error from the provider | `oauth?.accessToken` read without the optional chain in `initContext`, so the OAuth flow itself threw |
| The provider rejects the client | The client id or secret in the extension's configuration does not match the app registered with the provider |
| The provider returns "invalid scope" | A scope declared only on a realtime trigger, which is not collected |
| Calls work, then start failing after a while | The token expired and `refreshToken` is not handling the provider's refresh correctly |
| `FR_EXT_OAUTH_SETUP` | `setupOauth2` declared twice, or an OAuth method invoked on an extension that does not declare it |

## Related

- [Service Structure](service-structure.md) - `configItems` and `initContext`
- [HTTP Requests](http-requests.md) - where to attach the token
- [Troubleshooting](troubleshooting.md) - error codes and what they mean
