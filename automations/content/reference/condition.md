<!-- GENERATED FILE — do not edit. Source: block-knowledge/condition.yaml. Regenerate: make refgen -->
# Condition

Branch the flow into Yes/No paths based on a logical test.
## How it works

An if/else fork. Evaluate a value against an operation; true -> Yes path, false -> No path.
## When to use it

Any boolean decision point (gate, guard, simple routing on a known value).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Value to Check | expression | Yes | The operand (block/trigger data, Initial Data, system values). |
| Value Data Type | dropdown | Yes | STRING \| INT \| DOUBLE \| BOOLEAN/CHECKBOX \| DATETIME \| IMAGE \| JSON Object/Array. |
| Operation | dropdown | Yes | Comparison operator (depends on data type, e.g. IS TRUE, IS NOT EMPTY, equals). |
| Parts (+) | repeatable |  | Multiple sub-conditions joined by AND/OR with priority brackets. |
## Behavior

- Evaluates to true/false; flow continues down the matching (Yes/No) connector.
- Multi-part conditions combine sub-results with AND/OR + bracket precedence.
## Things to watch for

- Yes path = true, No path = false.
- Multi-part: AND/OR connector chips toggle; parentheses set precedence.
- Can compare via Operation OR build the comparison inside the expression (op IS TRUE).
## Related

- [Value Router](value-router.md)
- [AI Router](ai-router.md)
- expression-editor
