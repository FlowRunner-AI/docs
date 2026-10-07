# Quick Start: Your First Extension (code)

When you finish this page, a block of your own, Get Movie Details, sits in the block palette of every flow in
your workspace and fetches a film from The Movie Database. You paste one file and run four CLI commands. If you
would rather describe the service and let Claude Code write it, take
[Quick Start: Your First Extension (with AI)](ai-assisted.md).

!!! note "What you need"
    - **Node.js and npm.** Node 20 or newer.
    - **A FlowRunner™ workspace** you can sign in to.
    - **A TMDB API key.** It is free: create an account at themoviedb.org, open **Settings**, choose **API**, and
      copy the value labelled **API Key**, a 32-character string. The longer **API Read Access Token** on the
      same page is not the one this service uses.

## What you are building

One action, Get Movie Details, that takes a movie id and returns what TMDB holds about the film. It lives in a
project on your machine, and once deployed it is a block wired after Start like any other:

![Start wired into the Get Movie Details block on the canvas, with the block's configuration panel showing the Test Panel, the TMDB Custom Extension it belongs to with its CONFIGURE button, Movie ID set to 693134, and Reference Result Data As reading Get Movie Details Result](../images/extend/block-in-flow.png)

## 1. Create the project

Open a terminal and enter the following command:

```bash
npx @flowrunner/cli@latest init -d my-extensions
cd my-extensions
```

The package is `@flowrunner/cli`; the command it installs is `flowrunner`, inside the project, which is why
every later command starts with `npx flowrunner`. If `init` offers to install the command globally, either
answer works - see [The FlowRunner CLI](cli.md#installing-it).

## 2. Connect it to your workspace

Run the following command:

```bash
npx flowrunner login
```

Your browser opens on a page headed **Authorize Cloud Code CLI**. Pick the workspace this project will deploy
to and choose ((Authorize)):

![The Authorize Cloud Code CLI page with the signed-in account at the top, the Workspace picker showing the selected workspace and its id, the Deploy Custom extensions permission, and the Deny and Authorize buttons above a note that the token expires in 30 days](../images/extend/cli-authorize-workspace-picker.png)

## 3. Scaffold the service

Run the following command:

```bash
npx flowrunner cs blank --id tmdb --name "TMDB" -y
```

It creates `services/tmdb/` with a `src/index.js` to fill in and a placeholder `public/icon.svg`, then offers
to deploy. Answer **n**; there is nothing to deploy yet.

## 4. Paste the extension code

Replace `services/tmdb/src/index.js` with this:

```js
const z = Flowrunner.z

const API_BASE_URL = 'https://api.themoviedb.org/3'

const ext = Flowrunner.createExtension({
  id         : 'tmdb',
  name       : 'TMDB',
  description: 'Look up movies and TV from The Movie Database.',
  logo       : '/icon.svg',

  configItems: z.object({
    apiKey: z.string().secret().label('API Key').describe('Your TMDB v3 API key, from Settings -> API'),
  }),

  initContext: ({ config }) => ({
    baseUrl: API_BASE_URL,
    apiKey : config.apiKey,
  }),

  apiRequest: async ({ url, query, context }) => {
    return Flowrunner.Request.get(`${ context.baseUrl }${ url }`)
      .query({ ...query, api_key: context.apiKey })
  },
})

ext.addAction({
  category   : 'TMDB',
  id         : 'getMovieDetails',
  label      : 'Get Movie Details',
  description: 'Returns everything TMDB holds about one movie.',
  params     : z.object({
    movieId: z.string().label('Movie ID').describe('TMDB numeric id, e.g. 693134'),
  }),
  result: {
    id          : 693134,
    title       : 'Dune: Part Two',
    tagline     : 'Long live the fighters.',
    release_date: '2024-02-27',
    runtime     : 167,
    vote_average: 8.133,
    genres      : [{ id: 878, name: 'Science Fiction' }, { id: 12, name: 'Adventure' }],
  },
  execute: async ({ params, apiRequest }) => {
    return apiRequest({ url: `/movie/${ params.movieId }` })
  },
})
```

What each part does:

- **`configItems`** is the form you fill in once on the extension's page in the workspace (step 6); the values
  arrive as `config`, so the key is never written into the file. `.secret()` masks it on that form.
- **`apiRequest`** is the one place HTTP happens, so every action sends the key the same way.
- **`addAction`** is the block: `label` is its name in the editor, `params` are its fields, `result` is a
  sample of what it returns.

## 5. Deploy it

Run the following command:

```bash
npx flowrunner deploy
```

```
Deploying custom extensions...

  Connecting to Flowrunner Prod cluster (https://app.flowrunner.ai)
  Workspace "Acme Production" (3F2A9C41-7B10-4E52-9D64-0C81A7F5B2E3)
  Found 1 service under services/.

  Deploying 1 service:
    - new service: tmdb (TMDB) - [13cc36e0841e] - packaged 3.1 KB

  Deployed 1 service to workspace "Acme Production" (3F2A9C41-7B10-4E52-9D64-0C81A7F5B2E3) — you can use it in a flow.
  Open Custom Extensions screen in the Flowrunner Console to configure it: https://app.flowrunner.ai/app/Acme%20Production/custom-extensions
```

The extension is now listed under **Custom Extensions** in the workspace navigation:

![The Custom Extensions screen in the workspace navigation, listing the deployed TMDB service with 1 method, the file path src/index.js and its source hash](../images/extend/custom-extensions-list-minimal.png)

## 6. Give the workspace your TMDB key

Open the service, go to ((Configuration)), paste your TMDB key and ((SAVE CONFIGURATION)). The field is masked
because of `.secret()`, and the description you gave it sits behind the question mark beside the label. This is
done once per workspace:

![The TMDB Configuration tab with the API Key field masked as dots, a Show value eye at its edge, a help icon beside the label, and the SAVE CONFIGURATION button below](../images/extend/configuration-tab-minimal.png)

## 7. Run it by hand

The ((Execute)) tab beside it runs the action with a value you type. Enter `693134` as `movieId` and choose
((EXECUTE)):

![The Execute tab with Get Movie Details selected, movieId set to 693134, and under Result the end of the returned JSON, scrolled to show release_date 2024-02-27, runtime 167, status Released, tagline Long live the fighters., title Dune: Part Two and vote_average 8.136](../images/extend/execute-tab-minimal.png)

## 8. Add the block to a flow

Open a flow, or create one, and type `movie` into the palette's ((Search)) box. Your action sits under
**Custom Extensions**, in the TMDB group:

![The block palette with "movie" typed in its Search box, showing the CUSTOM EXTENSIONS group, the TMDB extension inside it, and Get Movie Details listed under Actions in the TMDB category](../images/extend/palette-getting-started.png)

Drag it onto the canvas after ((Start)) and set ((Movie ID)) to `693134`.

## 9. Run it in the flow

Choose ((run block)) in the ((Test Panel)). The **Test Monitor** shows what you sent and what TMDB returned:

![The Test Monitor's Block Results tab for Get Movie Details, with Input showing movieId 693134 and Output marked Success above the returned JSON, scrolled to its last lines: spoken_languages, status Released, tagline Long live the fighters., title Dune: Part Two, vote_average 8.136 and vote_count](../images/extend/test-monitor-result.png)

That is the extension running in your workspace.

## What to try next

- **Read the result from a later block.** In any block after it, open the Expression Editor and choose
  **Get Movie Details Result** under ((Block Data)). After the run in step 9 it lists everything TMDB
  returned. Double-click `title` and the expression reads {{Get Movie Details Result->title}}, which gives
  `Dune: Part Two`:

    ![The Expression Editor's Block Data tab with Get Movie Details Result opened: $$root and the fields TMDB returned in the run, each with its value, among them release_date 2024-02-27, runtime 167, tagline Long live the fighters. and title Dune: Part Two; the expression on the right reads Get Movie Details Result->title in double braces](../images/extend/result-block-data.png)

- **Add a second action** with another `addAction` call - [Actions](actions.md).
- **Add a trigger** that watches TMDB for new releases and starts a run - [Triggers](triggers.md).
- **Test it without deploying.** The project has a test harness that runs the extension with HTTP intercepted -
  [Testing](testing.md).
- **Change it and deploy again.** Every later change is `npx flowrunner deploy`; an editor that is already open
  picks the new version up on its own. Versions, rollback and what a deploy does -
  [Deploying & Managing](deploying.md).
- **When something fails** - [Troubleshooting](troubleshooting.md).

## Related

- [The FlowRunner CLI](cli.md) - every command and flag
- [Service Structure](service-structure.md) - `createExtension` in full: config, `initContext`, `apiRequest`
- [Parameters & Types](parameters-and-types.md) - every field type a param or config item can have

<!-- 2026-10-06 RECHECK ON PROD AS A CUSTOMER (staff mode off), @flowrunner/cli 0.1.4:
     STEP 1: the old `npx @flowrunner/cli init -d my-extensions` pinned the project to 0.1.1 because npx runs a globally
     installed copy when the spec has no version (FR-3710 - closed by Mark the same day as not an issue; `@latest` kept in the command, explanation removed).
     STEP 2: login (URL captured, approved in the automation browser): Authorize Cloud Code CLI page, Workspace picker
     with search, Deploy Custom extensions, Deny/Authorize (Authorize enabled after a pick), 30-day note; "This project
     is now connected to the workspace ..."; flowrunner.json gets workspaceId/workspaceName; .gitignore has .flowrunner/.
     STEP 3: cs blank output as described; deploy prompt answered n. STEP 4: the page's js block, run through the
     sandbox with nock -> {"id":693134,"title":"Dune: Part Two"} (api_key sent as a query param).
     STEP 5: RE-RUN after Mark's OK (2026-10-06): same code, CLI 0.1.4 scaffold -> "modified service: tmdb (TMDB) -
     [13cc36e0841e] - packaged 3.1 KB" (modified because TMDB already existed; a reader's first deploy says "new
     service" with the same hash and size). Sample output updated. The saved API key survived the deploy (32 chars,
     Execute still returns Dune: Part Two); Versions tab: 13cc36e0841e Active, older ones keep Activate.
     custom-extensions-list-minimal.png recaptured (staff view - Mark: document features as available; Open-Meteo
     row hidden by DOM so it shows a single-extension workspace; workspace name swapped to Acme Production; 99+ badge
     hidden). STEP 6: Configuration tab masked (disc), tooltip = the .describe() text,
     SAVE CONFIGURATION. STEP 7: Execute -> full TMDB JSON (~12 s). STEP 8: palette as described. STEP 9: run block
     -> Success. The Custom Extensions page opens by URL, but its NAV ITEM is hidden for customers
     (newCustomFlowExtensions = 0) - FOR-MARK decision 1.
     WHAT TO TRY NEXT: rewritten for the customer editor (text tokens; the "Select property" dialog is the staff-only
     D&D editor). Block Data after the run lists the full returned JSON; dblclick title inserts
     {{Get Movie Details Result->title}}; shot result-block-data.png (prod, customer view, read back).
     The Movie Details flow showed a stale "Model name for Api Service action" Not Ready (FR-3310 comment); it is
     Ready again after an edit. -->
<!-- 2026-09-30: STEP 1 RE-RUN VERBATIM on @flowrunner/cli 0.1.3 in an empty dir - works (FR-3686 fixed in 0.1.1);
     Server https://app.flowrunner.ai; `cs blank --id tmdb --name "TMDB" -y` works. -->
<!-- UPDATE 2026-09-29: STEP 1 now reads `npx @flowrunner/cli init -d my-extensions` (package renamed, FR-3686;
     prod is the default, FR-3632 fixed, so -s prod is gone). The same command under flowrunner-cli 0.1.0 was
     re-driven (Server https://app.flowrunner.ai). @flowrunner/cli 0.1.0 itself fails at init (FR-3686), so re-run
     STEP 1 VERBATIM once it is fixed. The bare-`flowrunner` "command not found" note below is superseded by the
     global launcher (cli.md's 2026-09-29 note). -->

<!-- DRIVE LOG for this page (rewritten 2026-09-22 as the code quick start; earlier logs superseded). Everything below
     was driven on 2026-09-22 unless dated otherwise. Environments: CLI drives in scratch projects (0.0.10 in
     ~/dev/fr-cli-docs-project; 0.0.12 fetched fresh by npx elsewhere); product drives on app.flowrunner.ai /
     Documentation Flows (Mark: docs verify against the released product), Playwright at 1680x1050, Mark signed in.
     STEP 1: `npx flowrunner-cli init -d my-extensions -s prod` run VERBATIM in an empty directory (0.0.12): stdout
     lists the ten files and prints `Server: https://app.flowrunner.ai`; flowrunner.json = {serverUrl prod}; git
     "Initial commit"; node_modules/.bin/flowrunner present. Without -s the same command binds to dev (FR-3632);
     `npx flowrunner init` (no -cli) is npm 404 - the package is flowrunner-cli, its bin is flowrunner. Bare
     `flowrunner` in a project: "command not found"; `npx flowrunner --version` works.
     STEP 2: `npx flowrunner login` -> Authorize Cloud Code CLI page (Authorize dimmed until a workspace is chosen);
     picked Documentation Flows, Authorize -> token written to .flowrunner/token (67 bytes), workspaceId/Name into
     flowrunner.json, .gitignore lists .flowrunner/. Shot cli-authorize-workspace-picker.png (prod, today; DOM
     substitutions: mark@backendless.com -> dev@acme.com, Mark Piller -> Alex Rivera, Documentation Flows -> Acme
     Production, workspace id -> the page's example id).
     STEP 3: `npx flowrunner cs blank --id tmdb --name "TMDB" -y` (fresh project, TTY via expect): creates services/,
     services/tmdb/{package.json,src/index.js,README.md,public/icon.svg}, then "Would you like to deploy ... (Y/n)"
     (default yes, not covered by -y, skipped without a TTY); answered n. Without -y it also asks Description, Enable
     OAuth2, Enable the Files API. `--id Bad_Id` is rejected with the message quoted on cli.md.
     STEP 4: the js block on this page (with .secret()) written verbatim to services/tmdb/src/index.js together with
     the one-test suite from testing.md; `npm test` -> 1 passed (also passes with `module.exports = ext` appended).
     STEP 5: bare `npx flowrunner deploy` in a one-service project (no prompt on a TTY): the block on this page is that
     run's stdout with workspace name/id swapped for the running example (also inside the console URL). Runs: new
     service 2464434ccfaf 3.9 KB; again -> "same service ... already deployed, nothing to upload"; description edited
     -> modified c05c7882b4cc; original restored -> modified 2464434ccfaf packaged again (an older hash is re-uploaded).
     Custom Extensions list: TMDB / 1 / src/index.js / SOURCE HASH 2464434c = first 8 chars. Shot
     custom-extensions-list-minimal.png (prod, today; nav name swapped to Acme Production).
     STEP 6: Configuration tab on prod: `.secret()` field masked by CSS (webkit-text-security: disc) with a "Show value"
     eye; Save Configuration is DOM "Save Configuration" uppercased by CSS. The .describe() text is a tooltip on the
     fa-circle-question icon beside the label (hover -> "Your TMDB v3 API key, from Settings -> API"); I first missed
     it (probed SVGs and body text only) and filed FR-3634, retracted the same day. Shot configuration-tab-minimal.png
     recaptured on prod today with a dummy value typed (demo-api-key-not-real, NOT saved) so the dots and the eye show.
     STEP 7: Execute tab lists the method, names the parameter by its key `movieId` and shows the description under
     the field. RUN on prod with Mark's v3 key (32 chars; his first paste was the 239-char v4 Read Access Token, which
     TMDB rejects and which surfaces as `{"error": "[object Object]"}` - FR-3637): movieId 693134 -> the full TMDB JSON
     in a scrollable Result box; shot execute-tab-minimal.png scrolled to the end so the title row is in frame.
     STEP 8: flow "Movie Details" created on prod (kept). Palette search box placeholder is "Search"; "movie" ->
     CUSTOM EXTENSIONS ("Custom JavaScript code extensions", FR-3474 live on prod) > TMDB (1) > Actions > TMDB > Get
     Movie Details; shot palette-getting-started.png. Also seen from a second flow (Weather Check): the group is there
     without a reload. Block dropped (elementId EXTENSION:::APP:::default:::tmdb:::getMovieDetails), auto-wired after
     Start; panel: Test Panel (run block / manage block result - DOM "Run Block", CSS lowercase), Name, "TMDB / Custom
     Extension" + CONFIGURE (opens the same API Key form in a dialog: "The configuration parameters will apply to all
     actions and triggers of the service"), Parameters: Movie ID [string] "(no value)" with "Movie ID is required"
     until filled, Reference Result Data As = "Get Movie Details Result", Assign to a Variable, Logging, Notes. Shot
     block-in-flow.png (Start anchor, block, panel to the Reference Result Data As row; minimap/controls/attribution
     hidden by CSS; viewport transform set by script).
     STEP 9: Run Block RUN on prod with the v3 key: Success; Input {"movieId":"693134"}; Output = TMDB's full JSON (63
     lines) in the Test Monitor's viewer; shot test-monitor-result.png scrolled so the title row is in frame (the viewer
     shows a few pixels of the line above its first full line - that is the editor's own scroll, not the crop). Editor
     refresh after a deploy DRIVEN: label changed to "Get Movie
     Details v2" + deploy -> the open editor's palette showed the new label without a reload (a placed block keeps its
     Name); restored + deploy -> palette back to the original label, again without a reload.
     WHAT TO TRY NEXT: Set Variables wired after the block; its Value field's Expression Editor: Block Data lists the
     pill "Get Movie Details Result"; dblclick inserts it; the token's arrow opens "Select property" listing the
     declared result sample with values and types (id 693134, title Dune: Part Two, tagline, release_date, runtime
     167, vote_average 8.133, genres array) BEFORE any run - shot result-property-picker.png; picking title writes
     the pill "Get Movie Details Result -> title". The picker's own box reads "Select or type...". Not run to a value.
     IMAGES: cli-authorize-workspace-picker.png, custom-extensions-list-minimal.png, palette-getting-started.png,
     block-in-flow.png, result-property-picker.png - prod, 2026-09-22, read back from pixels. configuration-tab-minimal.png,
     configuration-tab-minimal.png - prod, 2026-09-22 (dummy value typed, not saved). execute-tab-minimal.png and
     test-monitor-result.png - prod, 2026-09-22, with Mark's real v3 key saved, both scrolled so the title row is in
     frame. All eight images on this page are prod captures from 2026-09-22.
     NOT DRIVEN: themoviedb.org's Settings > API labels (Mark's paste confirmed the v4 token sits beside the v3 key);
     config value surviving a redeploy; the Expression pill evaluated to a value.
     DEFECTS FROM THESE DRIVES: FR-3632 (init defaults to dev), FR-3635 (z.number() decimals dropped at run time -
     this page's only param is a string). FR-3634 retracted (see STEP 6). -->
