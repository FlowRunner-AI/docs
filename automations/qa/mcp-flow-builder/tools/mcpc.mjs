#!/usr/bin/env node
// Drives the FlowRunner MCP Flow Builder directly with the MCP SDK (the same OAuth client registration as replay.mjs).
// Runs a list of steps in ONE MCP session, logs every call to <cache>/sdk-run-<date>.jsonl, prints a compact view.
//
// Usage:  node mcpc.mjs steps.json [--show 1500]      (steps.json: [{ tool, args, save?: { name: "dot.path" }, show? }])
//         node mcpc.mjs --probe 20 [--gap 2000]       (session-stability probe: list_workspaces N times, gap ms apart)
// Args may contain ${name} placeholders filled from earlier `save` entries (whole-string match keeps the value's type).
// Workspace boundary: any step whose args carry a workspaceId other than env.json's is refused before it is sent.

import fs from 'node:fs'
import path from 'node:path'
import http from 'node:http'
import { fileURLToPath } from 'node:url'
import { Client } from '@modelcontextprotocol/sdk/client/index.js'
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js'
import { UnauthorizedError } from '@modelcontextprotocol/sdk/client/auth.js'

const here = path.dirname(fileURLToPath(import.meta.url))
const cacheDir = process.env.MCP_QA_CACHE ? path.resolve(process.env.MCP_QA_CACHE) : path.resolve(here, '../../../.cache/mcp-qa')
const argv = process.argv.slice(2)
const flag = (n, d) => { const i = argv.indexOf(`--${n}`); return i >= 0 ? (argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : true) : d }
const MCP_URL = process.env.MCP_URL || 'https://dev.flowrunner.ai/mcp'
const env = JSON.parse(fs.readFileSync(path.join(cacheDir, 'env.json'), 'utf8'))
const CALLBACK_PORT = 8765
const logPath = path.join(cacheDir, `sdk-run-${new Date().toISOString().slice(0, 10)}.jsonl`)
const log = (rec) => fs.appendFileSync(logPath, JSON.stringify({ ts: new Date().toISOString(), ...rec }) + '\n')

const oauthPath = path.join(cacheDir, 'replay-oauth.json')
const readOauth = () => fs.existsSync(oauthPath) ? JSON.parse(fs.readFileSync(oauthPath, 'utf8')) : {}
const writeOauth = (patch) => fs.writeFileSync(oauthPath, JSON.stringify({ ...readOauth(), ...patch }, null, 2))
let codeResolver = null
const callbackServer = http.createServer((req, res) => {
  const u = new URL(req.url, `http://localhost:${CALLBACK_PORT}`)
  if (u.pathname === '/callback') { res.writeHead(200); res.end('Authorization received. You can close this tab.'); codeResolver?.(u.searchParams.get('code')) }
  else { res.writeHead(404); res.end() }
})
const provider = {
  get redirectUrl() { return `http://localhost:${CALLBACK_PORT}/callback` },
  get clientMetadata() { return { client_name: 'FlowRunner MCP QA replay', redirect_uris: [this.redirectUrl], grant_types: ['authorization_code', 'refresh_token'], response_types: ['code'], token_endpoint_auth_method: 'none' } },
  clientInformation() { return readOauth().clientInformation },
  saveClientInformation(info) { writeOauth({ clientInformation: info }) },
  tokens() { return readOauth().tokens },
  saveTokens(tokens) { writeOauth({ tokens }) },
  redirectToAuthorization(url) { fs.writeFileSync(path.join(cacheDir, 'replay-auth-url.txt'), url.toString()); console.error('[oauth] authorization needed; URL written to .cache/mcp-qa/replay-auth-url.txt') },
  saveCodeVerifier(v) { writeOauth({ codeVerifier: v }) },
  codeVerifier() { return readOauth().codeVerifier },
}

async function connect() {
  const client = new Client({ name: 'flowrunner-mcp-qa-driver', version: '0.2.0' })
  let transport = new StreamableHTTPClientTransport(new URL(MCP_URL), { authProvider: provider })
  try { await client.connect(transport) } catch (e) {
    if (!(e instanceof UnauthorizedError)) throw e
    await new Promise((r) => callbackServer.listen(CALLBACK_PORT, r))
    const code = await new Promise((r) => { codeResolver = r })
    await transport.finishAuth(code); callbackServer.close()
    transport = new StreamableHTTPClientTransport(new URL(MCP_URL), { authProvider: provider })
    await client.connect(transport)
  }
  return { client, transport }
}

const text = (res) => (res?.content || []).map((c) => c.text || '').join('')
const tryJson = (t) => { try { return JSON.parse(t) } catch { return undefined } }
const get = (obj, p) => p.split('.').reduce((o, k) => (o == null ? o : o[k]), obj)
const vars = {}
const fill = (v) => {
  if (typeof v === 'string') {
    const whole = v.match(/^\$\{([\w.]+)\}$/); if (whole) return vars[whole[1]]
    return v.replace(/\$\{([\w.]+)\}/g, (_, k) => String(vars[k]))
  }
  if (Array.isArray(v)) return v.map(fill)
  if (v && typeof v === 'object') return Object.fromEntries(Object.entries(v).map(([k, x]) => [k, fill(x)]))
  return v
}
const wsIds = (o, acc = []) => { if (o && typeof o === 'object') for (const [k, v] of Object.entries(o)) { if (k === 'workspaceId') acc.push(v); else wsIds(v, acc) } return acc }

// FR-3687 workaround: dev answers ~half of requests with 404 "Session not found" (session unknown to the instance that
// serves the request). The 404 is returned before the tool runs, so reconnecting with a fresh session and resending is safe.
const isSessionLost = (e) => /Session not found|code: 404|-32001|503 Service Temporarily Unavailable|502 Bad Gateway/.test(String(e?.message || e) + String(e?.code || ''))
const pause = (ms) => new Promise((r) => setTimeout(r, ms))
let retries = 0
async function connectRetry() {
  for (let a = 0; a < 15; a++) { try { return await connect() } catch (e) { if (!isSessionLost(e)) throw e; retries++; if (/50[23]/.test(String(e?.message))) await pause(5000) } }
  throw new Error('could not establish an MCP session in 15 attempts')
}
let { client, transport } = await connectRetry()
async function callTool(name, args) {
  for (let a = 0; a < 15; a++) {
    try { return await client.callTool({ name, arguments: args }, undefined, { timeout: 180000 }) }
    catch (e) { if (!isSessionLost(e)) throw e; retries++; if (/50[23]/.test(String(e?.message))) await pause(5000); try { await client.close() } catch {} ;({ client, transport } = await connectRetry()) }
  }
  throw new Error('session lost 15 times in a row')
}
console.error(`[mcpc] connected; log ${path.basename(logPath)}`)

if (flag('tools')) {
  const info = client.getServerVersion?.()
  const res = await client.listTools()
  console.log('server', JSON.stringify(info))
  console.log('tools', res.tools.length)
  for (const t of res.tools) console.log(' -', t.name, '|', (t.description || '').split('\n')[0].slice(0, 110))
  await client.close(); process.exit(0)
}
if (flag('probe')) {
  const n = Number(flag('probe')), gap = Number(flag('gap', 2000))
  for (let i = 0; i < n; i++) {
    const t0 = Date.now()
    try { const r = await client.callTool({ name: 'list_workspaces', arguments: {} }); console.log(i, 'ok', Date.now() - t0, 'ms', r.isError ? 'isError' : '') ; log({ probe: i, ok: true }) }
    catch (e) { console.log(i, 'FAIL', Date.now() - t0, 'ms', String(e.message || e).slice(0, 300)); log({ probe: i, ok: false, error: String(e.message || e) }) }
    await new Promise((r) => setTimeout(r, gap))
  }
  await client.close(); process.exit(0)
}

const steps = JSON.parse(fs.readFileSync(argv[0], 'utf8'))
const showDefault = Number(flag('show', 1500))
for (const [i, s] of steps.entries()) {
  const args = fill(s.args || {})
  const bad = wsIds(args).filter((w) => w !== env.workspaceId)
  if (bad.length) { console.log(`#${i} ${s.tool} REFUSED: workspace ${bad[0]} is outside Documentation Flows`); log({ i, tool: s.tool, refused: bad }); continue }
  let res, err
  const t0 = Date.now()
  try { res = await callTool(s.tool, args) } catch (e) { err = String(e.message || e) }
  const t = err ? `TRANSPORT ERROR: ${err}` : text(res)
  log({ i, label: s.label, tool: s.tool, args, isError: !!res?.isError, ms: Date.now() - t0, text: t })
  const j = tryJson(t)
  if (s.save && j) for (const [k, p] of Object.entries(s.save)) vars[k] = get(j, p)
  const show = s.show ?? showDefault
  console.log(`\n#${i} ${s.label ? `[${s.label}] ` : ''}${s.tool}${res?.isError ? '  isError' : ''}  (${Date.now() - t0} ms)`)
  if (show > 0) console.log(t.length > show ? t.slice(0, show) + ` …[+${t.length - show}]` : t)
  if (s.stopOnError && (err || res?.isError)) break
}
if (Object.keys(vars).length) console.log('\n[vars]', JSON.stringify(vars))
console.error(`[mcpc] session-lost retries: ${retries}`)
await client.close()
