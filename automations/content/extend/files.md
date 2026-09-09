# Storing Files

An extension that produces a file - a rendered PDF, an export, an image it generated, a report it fetched
from a provider - has nowhere to put it. A handler's return value goes into the flow as data, and a buffer
is not data a flow can carry. The Files API is the storage that fills that gap: your handler writes the
bytes, and what it hands back to the flow is a URL the next block can use.

## Turning it on

File storage is opt-in. Declare it on the extension:

```javascript
const vault = Flowrunner.createExtension({
  id             : 'filevault',
  name           : 'File Vault',
  usesFileStorage: true,
})
```

With that set, handlers receive a `files` client in their context alongside `params` and `config`, and
`filesScope`, which names the three storage layers so a scope is a constant rather than a string you could
misspell:

```javascript
vault.addAction({
  category   : 'File Vault',
  id         : 'saveDocument',
  label      : 'Save Document',
  description: 'Writes text to a file in the workspace file storage and returns its URL.',
  params     : z.object({
    filename: z.string().label('Filename'),
    content : z.text().label('Content'),
  }),
  result : { url: 'https://files.example.com/notes.txt', size: 12 },
  execute: async ({ params, files, filesScope }) => {
    const saved = await files.uploadFile(Buffer.from(params.content), {
      scope   : filesScope.WORKSPACE,
      filename: params.filename,
      ttl     : 3600,
    })

    return { url: saved.url, size: saved.size }
  },
})
```

Without `usesFileStorage`, `files` is a stand-in that throws the moment a handler touches it, rather than
failing later with something harder to place - the error is `FR_EXT_FEATURE_NOT_ENABLED` (see
[Troubleshooting](troubleshooting.md)).

## Choosing where a file lives

Every call takes a `scope`, and the scope decides how long the file stays reachable and who else can see
it. This is the decision to make first, because it is the one you cannot change afterwards without moving
the file:

| Scope | The file belongs to | Reach for it when |
| --- | --- | --- |
| `WORKSPACE` | The whole workspace. It outlives every flow and every run. | The file is a shared asset - a template, a logo, a reference list that many flows read. |
| `FLOW` | One flow, shared by all of its runs. This is the default. | Runs of the same flow build on each other's output - a rolling export, a cache a later run reads. |
| `EXECUTION` | A single run. | The file is working material for this run alone - an attachment fetched, transformed, and handed on. |

`FLOW` is the default because it is the common case: a file that belongs to the automation rather than to
the workspace or to one run. Name a scope as `filesScope.WORKSPACE`, `filesScope.FLOW` or
`filesScope.EXECUTION`; the plain strings work too.

**`FLOW` and `EXECUTION` exist only inside a run.** Both are addressed by the running flow, and `EXECUTION`
by the run itself, so a method invoked where there is no run has neither: a dictionary or a loader called
while someone configures a block, an OAuth step, a method run by hand from the extension's page. There
the default `FLOW` scope fails with `Flow scope requires flowId`. Use `WORKSPACE` for anything such a
method reads or writes - which is why the example above does - and keep `FLOW` and `EXECUTION` for work
done by a block in a flow. `usage()` is always workspace-wide, so it works everywhere.

The token the client presents is issued per invocation and lives about fifteen minutes. A method that waits
longer than that before its first file call can find the call refused, so do the file work before a long
wait rather than after it.

## The five calls

```javascript
await files.uploadFile(buffer, options)   // write bytes, get a URL back
await files.list(options)                 // what is in this scope
await files.get(filename, options)        // one file's details and URL
await files.delete(filename, options)     // remove it
await files.usage()                       // how much of the quota is used
```

**`uploadFile(file, options)`** takes a `Buffer` or a `Uint8Array`.

| Option | Meaning |
| --- | --- |
| `scope` | Where the file lives. Defaults to `FLOW`. |
| `filename` | The name to store it under. Without one the file is stored as `file`. |
| `generateUrl` | Whether to return a download URL. **Defaults to `true`** - leave it alone unless you have a reason, because a `false` here returns a null `url` while the upload still reports success. |
| `ttl` | How long the returned URL stays valid, in seconds. |
| `objectTtl` | How long the stored file itself is kept, in seconds. Without it the file stays until something deletes it. |
| `overwrite` | Whether an existing file of that name is replaced. Without it you get a second stored object rather than a replacement. |

The two lifetimes are separate on purpose: `ttl` expires the link, `objectTtl` expires the file. A short
`ttl` on a long-lived file just means the next reader asks for a fresh URL.

It returns the stored file's `key` and `filename`, its `url` and `size`, `urlExpiresAt`,
`objectExpiresAt` (null when no `objectTtl` was set), and `overwritten`.

**`list(options)`** takes `scope`, `limit` and `cursor`, plus `ttl` and `generateUrl` for the URLs it
returns. It answers with `files`, a `cursor`, and `hasMore` - page by passing the cursor back until
`hasMore` is false. Each entry carries `key`, `filename`, `url`, `size`, `createdAt`, `urlExpiresAt` and
`objectExpiresAt`.

**`get(filename, options)`** takes `scope`, `ttl` and `generateUrl`, and returns one of those same
entries. This is how you hand an already-stored file a fresh URL.

**`delete(filename, options)`** takes `scope` and answers with `key`, `deleted`, and `freedBytes`.

**`usage()`** takes nothing and reports the workspace's storage as a whole: `usedBytes` and `quotaBytes`
with `usedFormatted` and `quotaFormatted` alongside them, `utilizationPercent`, and `fileCount`. Use it to
fail early with a clear message instead of letting an upload fail against the quota.

## Testing against a stub

The sandbox the CLI scaffolds provides `createFilesSandbox()`, so a service that stores files can be run
locally without touching real storage - see [Testing](testing.md). Hosts can substitute a client the same
way, which is what lets a suite point file storage at a local backend.

!!! warning "Not working from a custom extension today"
    File storage runs in the Shared Extensions the platform ships. From a custom extension the same call
    currently fails inside the workspace's Cloud Code pod before it reaches storage, so an extension that
    declares `usesFileStorage: true` errors the first time a handler touches `files`. Design around URLs
    until that is resolved: pass a provider's URL through, or fetch the bytes and forward them, and let a
    storage-capable block persist the result.

## Related

- [Service Structure](service-structure.md) - where `usesFileStorage` sits among the other factory props
- [Actions](actions.md) - the rest of the handler context `files` arrives in
- [Testing](testing.md) - the sandbox, including its file backend
- [Troubleshooting](troubleshooting.md) - `FR_EXT_FEATURE_NOT_ENABLED` and the other typed errors

<!-- REVISED 2026-09-09 for FR-3420 (flowrunner-cli 0.0.8+, fr-cloud-code 0.0.6), Documentation Flows on
     dev.flowrunner.ai. DRIVEN: a `filevault` service with usesFileStorage:true and the Save Document action
     above (scope filesScope.WORKSPACE) was deployed (571c4092e566) and run from Custom Extensions > File Vault
     > Execute. Result: {"error":"getaddrinfo ENOTFOUND fr-automation"} - the pod cannot resolve the file
     service host; a TMDB action from the same pod in the same minute succeeded, so it is the file path
     alone. Reported on FR-3420 (comment 2026-09-09). The warning therefore STAYS, reworded to what fails now.
     filesScope, the scope-outside-a-run rule and the ~15-minute token are from the shipped 10-files-api.md
     and the console guide's files.md (FR-3420 commit), not driven. -->

<!-- FR-3412 (New Extensions Runner) - the Files API half, which Mark asked for explicitly on 2026-08-31
     ("Yes, we must document Files API for extensions"), in the same breath as ruling the LEGACY format
     out of the docs ("we never documented legacy format for extensions. No one knows about them").
     This page therefore documents ONLY the v2 `ctx.files` client and never `this.flowrunner.Files.*`.
     SOURCED FROM THE RUNNER ITSELF, not from the ticket and not from the console docs on GitHub (which
     are unreachable from here):
       console/flow-extension-runner/src/common/context-files.ts  - the FilesApi interface (the five
         methods, verbatim), FileScope (WORKSPACE | FLOW | EXECUTION), the option interfaces
         (UploadFileOptions / ListOptions / GetOptions / DeleteOptions), the result interfaces
         (UploadResult / FileInfo / ListResult / DeleteResult / UsageResult), the scope->path mapping
         and its two thrown messages, the `generateUrl = true` and `scope = FLOW` defaults, and the base
         path {serverURL}/{appId}/{apiKey}/v1/files.
       console/flow-extension-runner/__tests__/fixtures/files-api.js - the authoring example this page's
         snippets follow, and the source of "usesFileStorage swaps the throwing `files` proxy for a real
         client".
     The `generateUrl: false` warning is not invented: SharedExtensions/docs/ai/defect-audit-2026-08-07.md
     CLASS 4 records 166 legacy services shipping a caller-overridable generateUrl, where the upload
     succeeds and the flow receives a null url. The v2 default closes it; the page says why it matters.
     The Custom Extensions admonition is FR-3412's own "Known gap", tracked as FR-3420.
     NOT DRIVEN IN-PRODUCT: no extension was built and run against real storage in this pass - the
     contract above is read from source, not exercised. Flagged to Mark as the one page here whose facts
     are source-derived rather than driven. -->
