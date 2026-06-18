// Playwright MCP init-script — fixes Ace editor worker loading in the automation browser.
//
// WHY: FlowRunner uses the Ace code editor, which spawns a blob web worker that does
// `importScripts('worker-<mode>.js')` resolved RELATIVE to the current page URL.
// The app is an SPA, so that path returns index.html (text/html), and the browser
// refuses to run it ("Refused to execute script ... MIME type ('text/html')").
// A normal browser has the worker cached/served; our fresh Playwright profile does not.
// These workers only do editor linting/validation — they are NOT involved in executing
// flows or Cloud Code. So we neutralize ONLY the Ace mode workers and leave every other
// worker (including anything flow/Cloud Code execution uses) untouched.
//
// This runs before the page's own scripts on every load, so the fix is durable across
// reloads (unlike a one-off page eval).

(function () {
  try {
    var aceWorkerRe = /worker-(base|coffee|css|html|javascript|json|lua|php|xml|xquery|yaml)\.js/i;
    var Orig = window.Worker;
    if (!Orig || Orig.__frAceFix) return;

    function makeStub() {
      return {
        onmessage: null, onerror: null, onmessageerror: null,
        postMessage: function () {}, terminate: function () {},
        addEventListener: function () {}, removeEventListener: function () {},
        dispatchEvent: function () { return false; }
      };
    }

    var Patched = function (url, options) {
      try {
        var s = String(url);
        if (s.indexOf('blob:') === 0) {
          var code = '';
          try {
            var x = new XMLHttpRequest();
            x.open('GET', s, false); // sync read of the blob worker source
            x.send();
            code = x.responseText || '';
          } catch (e) {}
          if (aceWorkerRe.test(code)) return makeStub(); // Ace lint worker only
        }
      } catch (e) {}
      return new Orig(url, options);
    };
    Patched.prototype = Orig.prototype;
    Patched.__frAceFix = true;
    window.Worker = Patched;
  } catch (e) {
    // never block page load on this fix
  }
})();
