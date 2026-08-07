// DOM PII-redaction for docs screenshots. Inject via Playwright browser_evaluate, then call
// __redact({...}) BEFORE taking the shot. Replaces real values with placeholders in visible text
// nodes and in input/textarea values, so emails / names / keys never reach a published image.
//
// Example:
//   __redact({ "mark@backendless.com": "you@example.com", "Mark Piller": "Alex Rivera" })
window.__redact = function (map) {
  const pairs = Object.entries(map);
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let node;
  while ((node = walker.nextNode())) {
    let t = node.nodeValue;
    for (const [from, to] of pairs) if (t.includes(from)) t = t.split(from).join(to);
    if (t !== node.nodeValue) node.nodeValue = t;
  }
  document.querySelectorAll("input, textarea").forEach((el) => {
    let v = el.value || "";
    for (const [from, to] of pairs) if (v.includes(from)) v = v.split(from).join(to);
    if (v !== el.value) el.value = v;
  });
  return "redacted";
};
