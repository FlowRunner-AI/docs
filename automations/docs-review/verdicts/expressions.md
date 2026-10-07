# Verdict: content/learn/concepts/expressions.md (Expression Editor)

## 2026-10-06 - release sweep "Without version/devtasks2" + "without3"

- Verdict: **major-rework** (concept-page-review wf_8c1860cb-24c, one run; not re-run). Mark decides ship.
- Scope: FR-3610 -> FR-3611 (fixVersion **v.1.1.3, unreleased**): Current date with a part (Year ... Second).

### The finding that changes the page (gate item 1, now CONFIRMED in-product)
Customers do not get the editor this page teaches. Driven on dev 2026-10-06 with System Developer Mode off
(localStorage Flowrunner.system_dev_mode=false): the Expression Editor has NO mode dropdown - only the text editor with
{{...}} tokens and "Type {{}} to auto-suggest". The pill editor with pencils ("New D&D Editor") appears only for staff
accounts: console-status flowrunnerNewDNDExpressionEditor is 0 on prod and dev, and the bundle adds the D&D option only when
that toggle is truthy (staff override). Affected on this page: the whole "Reaching inside a result the Editor has not seen"
section (pencil, path row, type button, index dropdown, "clicking the body of a pill selects it") and its three shots.
Every shot on the page shows a "New Editor" mode dropdown customers never see. Decision for Mark (in the hand-off).

### Release delta - resolved after the gate
- Items 1, 5, 6, 7 (Current date): rewritten for the customer's editor and DRIVEN as a customer: double-click Current date
  -> {{Current date->}} (the full date and time); cursor after the arrow -> auto-suggest lists exactly Year, Month, Date,
  Week Number, Week Day, Hour, Minute, Second. New shot ee-current-date-parts.png (customer view, read back). Paragraph
  moved after ee-composed so the groups list -> ee-variables -> "So a subject line..." order is restored. The reference
  is the {{...}} wand token, not code. Value formats (ISO text, numbers, Monday = 1) remain SOURCE (FR-3611 engineer
  comment); run-time values and the weekend Condition NOT driven.

### Owed on prod (batched session)
- Current date in the customer editor on app.flowrunner.ai (FR-3611 is v.1.1.3 in Jira).

### Older debt carried
- Live Preview taught as resolving values; pixels show pills (2); core idea never shown on one example (3, 16);
  ee-variables.png is a real customer's banking flow and has no Current date chip (4); scope / Related (8);
  Text | HTML switch (9); ledger (10); path-row section craft and undriven claims (11-14, moot if the D&D decision drops it);
  date values bullet (15); JSON Editor + quoting rule (17, 18); FR-1505 schema-aware (19); auto-suggest gesture (20);
  Flow Context wording + callback group (21); ((APPLY)) (22); exploration logs (23).
