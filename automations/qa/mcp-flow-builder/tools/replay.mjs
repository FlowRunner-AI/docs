#!/usr/bin/env node
// Replays a recorded FlowRunner MCP Flow Builder session (JSONL written by record-hook.sh)
// against a live endpoint, remapping server-generated ids and asserting result shapes.
//
// Usage:
//   node replay.mjs --log ../../../.cache/mcp-qa/run-2026-09-01.jsonl --from 12 --to 24 [--suffix " (replay)"] [--dry]
//   env: MCP_URL (default https://dev.flowrunner.ai/mcp), ENV_JSON (default ../../../.cache/mcp-qa/env.json)
//
// OAuth: first run prints an authorization URL and writes it to <cache>/replay-auth-url.txt; open it in a
// browser logged in on the same host, authorize, and the localhost callback completes the flow. Tokens and the
// dynamic client registration are cached in <cache>/replay-oauth.json.

import fs from 'node:fs'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js'
import { UnauthorizedError } from '@modelcontextprotocol/sdk/client/auth.js'

const here = path.dirname(fileURLToPath(import.meta.url))
const cacheDir = path.resolve(here, '../../../.cache/mcp-qa')
const args = Object.fromEntries(process.argv.slice(2).map((a, i, arr) => a.startsWith('--') ? [a.slice(2), arr[i + 1] && !arr[i + 1].startsWith('--') ? arr[i + 1] : true] : []).filter(Boolean))

const MCP_URL = process.env.MCP_URL || 'https://dev.flowrunner.ai/mcp'
const envPath = process.env.ENV_JSON || path.join(cacheDir, 'env.json')
const env = JSON.parse(fs.readFileSync(envPath, 'utf8'))
const logPath = path.resolve(process.cwd(), args.log || path.join(cacheDir, 'run-2026-09-01.jsonl'))
const from = Number(args.from ?? 0)
const to = Number(args.to ?? Infinity)
const suffix = typeof args.suffix === 'string' ? args.suffix : ' (replay)'
const dry = !!args.dry
const CALLBACK_PORT = Number(process.env.CALLBACK_PORT || 8765)
const PREFIX = 'mcp__flowrunner-dev__'
const ID_KEYS = ['nodeId', 'id', 'flowId', 'versionId', 'caseId', 'decisionId', 'toolId', 'flowElementId']

// ---------- OAuth provider (PKCE, dynamic client registration, localhost callback) ----------
const oauthPath = path.join(cacheDir, 'replay-oauth.json')
const readOauth = () => fs.existsSync(oauthPath) ? JSON.parse(fs.readFileSync(oauthPath, 'utf8')) : {}
const writeOauth = (patch) => fs.writeFileSync(oauthPath, JSON.stringify({ ...readOauth(), ...patch }, null, 2))

let pendingCode = null
let codeResolver = null
const callbackServer = http.createServer((req, res) => {
  const u = new URL(req.url, `http://localhost:${CALLBACK_PORT}`)
  if (u.pathname === '/callback') {
    pendingCode = u.searchParams.get('code')
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.end('Authorization received. You can close this tab.')
    if (codeResolver) codeResolver(pendingCode)
  } else { res.writeHead(404); res.end() }
})

const provider = {
  get redirectUrl() { return `http://localhost:${CALLBACK_PORT}/callback` },
  get clientMetadata() {
    return { client_name: 'FlowRunner MCP QA replay', redirect_uris: [`http://localhost:${CALLBACK_PORT}/callback`], grant_types: ['authorization_code', 'refresh_token'], response_types: ['code'], token_endpoint_auth_method: 'none' }
  },
  clientInformation() { return readOauth().clientInformation },
  saveClientInformation(info) { writeOauth({ clientInformation: info }) },
  tokens() { return readOauth().tokens },
  saveTokens(tokens) { writeOauth({ tokens }) },
  redirectToAuthorization(url) {
    fs.writeFileSync(path.join(cacheDir, 'replay-auth-url.txt'), url.toString())
    console.error(`\n[oauth] Open this URL in a browser logged in on ${new URL(MCP_URL).origin} and click Authorize:\n${url}\n(also written to ${path.join(cacheDir, 'replay-auth-url.txt')})`)
  },
  saveCodeVerifier(v) { writeOauth({ codeVerifier: v }) },
  codeVerifier() { return readOauth().codeVerifier },
}

async function connect() {
  const client = new Client({ name: 'flowrunner-mcp-qa-replay', version: '0.1.0' })
  let transport = new StreamableHTTPClientTransport(new URL(MCP_URL), { authProvider: provider })
  try {
    await client.connect(transport)
  } catch (e) {
    if (!(e instanceof UnauthorizedError)) throw e
    await new Promise((res) => callbackServer.listen(CALLBACK_PORT, res))
    const code = pendingCode || await new Promise((res) => { codeResolver = res })
    await transport.finishAuth(code)
    callbackServer.close()
    transport = new StreamableHTTPClientTransport(new URL(MCP_URL), { authProvider: provider })
    await client.connect(transport)
  }
  return client
}

// ---------- recording ----------
function loadRecords() {
  const lines = fs.readFileSync(logPath, 'utf8').split('\n').filter(Boolean).map((l) => JSON.parse(l))
  return lines.map((r, i) => ({ i, tool: (r.tool_name || '').replace(PREFIX, ''), input: r.tool_input || {}, text: responseText(r.tool_response), ts: r.ts }))
}
function responseText(resp) {
  if (!resp) return ''
  if (Array.isArray(resp)) return resp.map((x) => x.text || '').join('')
  if (resp.content) return resp.content.map((x) => x.text || '').join('')
  return typeof resp === 'string' ? resp : JSON.stringify(resp)
}
const parse = (t) => { try { return JSON.parse(t) } catch { return undefined } }
const isErrText = (t) => /^(ERROR|BAD_REQUEST|NOT_FOUND|VALIDATION_ERROR|INVALID_OPERATION):/.test(t.trim())

// ---------- id remapping ----------
const idMap = new Map() // recorded id -> live id
function remap(value) {
  if (typeof value === 'string') {
    if (idMap.has(value)) return idMap.get(value)
    // ids embedded in {{...}} text are aliases, not ids — leave them
    return value
  }
  if (Array.isArray(value)) return value.map(remap)
  if (value && typeof value === 'object') return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, remap(v)]))
  return value
}
function learnIds(recorded, live) {
  if (!recorded || !live || typeof recorded !== 'object' || typeof live !== 'object') return
  if (Array.isArray(recorded) && Array.isArray(live)) { recorded.forEach((r, i) => learnIds(r, live[i])); return }
  for (const k of Object.keys(recorded)) {
    const rv = recorded[k], lv = live[k]
    if (ID_KEYS.includes(k) && typeof rv === 'string' && typeof lv === 'string' && rv !== lv) idMap.set(rv, lv)
    else if (rv && typeof rv === 'object') learnIds(rv, lv)
  }
}
const shapeOf = (j) => j === undefined ? 'text' : Array.isArray(j) ? `array[${j.length}]` : j && typeof j === 'object' ? Object.keys(j).sort().join(',') : typeof j

// ---------- main ----------
const records = loadRecords().filter((r) => r.i >= from && r.i <= to && r.tool)
console.error(`[replay] ${records.length} calls from ${path.basename(logPath)} [${from}..${to}] against ${MCP_URL}`)
if (dry) { for (const r of records) console.log(r.i, r.tool, JSON.stringify(r.input).slice(0, 120)); process.exit(0) }

const client = await connect()
const ws = await client.callTool({ name: 'list_workspaces', arguments: {} })
const wsList = parse(responseText(ws.content ? ws : { content: ws.content })) || parse(ws.content?.[0]?.text)
if (!Array.isArray(wsList) || !wsList.some((w) => w.id === env.workspaceId)) {
  console.error(`[replay] REFUSING: workspace ${env.workspaceId} (${env.workspaceName}) not in list_workspaces for this token`); process.exit(2)
}
const results = []
for (const r of records) {
  let input = remap(r.input)
  // every recorded workspaceId is replaced by the authorized one, never anything else
  input = JSON.parse(JSON.stringify(input).replaceAll(/"workspaceId":"[^"]+"/g, `"workspaceId":"${env.workspaceId}"`))
  if (r.tool === 'create_flow' && typeof input.name === 'string' && !input.name.endsWith(suffix)) input.name = input.name + suffix
  let live, liveText, liveErr = false
  try {
    live = await client.callTool({ name: r.tool, arguments: input })
    liveText = responseText(live); liveErr = !!live.isError || isErrText(liveText)
  } catch (e) { liveText = String(e.message || e); liveErr = true }
  const recJ = parse(r.text), liveJ = parse(liveText)
  const recErr = isErrText(r.text)
  if (!liveErr) learnIds(recJ, liveJ)
  const same = {
    error: recErr === liveErr,
    shape: shapeOf(recJ) === shapeOf(liveJ),
    issues: JSON.stringify(recJ?.issues ?? null) === JSON.stringify(liveJ?.issues ?? null),
    status: (recJ?.status ?? null) === (liveJ?.status ?? null),
  }
  const ok = Object.values(same).every(Boolean)
  results.push({ i: r.i, tool: r.tool, ok, same, liveText: liveText.slice(0, 140).replace(/\s+/g, ' ') })
  console.error(`${ok ? 'OK  ' : 'DIFF'} #${r.i} ${r.tool} ${ok ? '' : JSON.stringify(same)}`)
}
const bad = results.filter((x) => !x.ok)
console.log('| # | tool | ok | error= | shape= | issues= | status= | live (truncated) |')
console.log('|---|---|---|---|---|---|---|---|')
for (const x of results) console.log(`| ${x.i} | ${x.tool} | ${x.ok ? '✅' : '❌'} | ${x.same.error} | ${x.same.shape} | ${x.same.issues} | ${x.same.status} | ${x.liveText.replaceAll('|', '/')} |`)
console.log(`\n${results.length - bad.length}/${results.length} calls matched the recording. id remaps learned: ${idMap.size}`)
await client.close()
process.exit(bad.length ? 1 : 0)
