# S5 — Countdown (Repeat loop, nested Condition, Break, Data Bucket counter)

Driven 2026-09-02 02:49–02:56 UTC · dev.flowrunner.ai · Documentation Flows.
Prompt: "Count down from 5 to 0 with a Repeat loop and stop early when the counter hits 2."

## Build
data-bucket "Init Counter" (Counter: counter=5 NUMBER, visited={{Empty List}}) → repeat "Count Down" (maxIterations 100, keep-looping
`{{Data Buckets:Counter - counter->}} > 0` INT) → nested: "Record Counter" arrays.add(visited, counter) → save to visited;
condition "Hit 2?" → then: break-repeat "Stop Early" / else: "Decrement" math.subtract(counter, 1) → save to counter;
→ return-result {visited, finalCounter}. Flow E554B13B-645B-48D3-98CB-098DF194A7DB, version 9BF7A4D8-DE0F-4317-BF96-10C3C4D1EE7D.
Negative probe: add_block(break-repeat) at top level → INVALID_OPERATION with the documented message. PASS.

## Oracles
- **O1:** group LOOP has `condition.conditionParts` (> 0) + `grouping`, firstElementId = Record Counter, maxIterations 100; nested Condition has
  then=BREAK, else=Decrement; both saveToVariable targets persisted (setResultToVariable set explicitly this time). PASS.
- **O2:** S5-o2-canvas.png.
- **O3:** run 1 (`equal` 2, INT): `{"finalCounter":0.0,"visited":[5,4.0,3.0,2.0,1.0]}` — break never fired.
  run 2 (`equal` 2, DOUBLE): same. run 3 (`<=` 2, DOUBLE): `{"finalCounter":2.0,"visited":[5,4.0,3.0,2.0]}` — PASS.

## Findings
1. **Engine:** Condition `equal` does not match a Double runtime value (2.0 from math.subtract) against the integer literal 2, for INT or
   DOUBLE propertyType. Comparison operators work. Not an MCP defect; needs docs/Jira check before filing (F-S5-1).
2. **Tool-doc defect:** set_condition_parts description example uses `operation: "greaterThan"`; the real ids are `>`, `<`, `>=`, `<=` (F-S5-2).
3. Bucket references in set_condition_parts fail with "could not resolve … against any known reference" until the bucket is wired upstream
   of the loop; the error wording suggests a typo rather than reachability (F-S5-3).
4. Each edit cycle required the Console's Stop button because stop_flow only pauses (F-S4-5 again, 2 more repros).
5. Q8 data point: keyword pills are saved WITH parentheses (`arrays.create()`), contradicting R11 (F-S5-5).

## Teardown
stop_flow(9BF7A4D8…) after run 3. Flow kept (engine-equality repro) for end-of-phase deletion.
