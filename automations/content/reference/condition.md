<!-- GENERATED FILE - do not edit. Source: block-knowledge/condition.yaml. Regenerate: make refgen -->
# Condition

This block tests a value and splits the flow into two paths based on the answer. The test either passes or fails, and the flow continues down the matching path.

## How it works

It is a yes-or-no fork in the flow. You give it a value to check, tell it what type that value is, and pick the comparison to run against it - for example whether a number is greater than another, or whether a checkbox is on. That comparison comes out true or false. A true result sends the flow down the block's **Yes** path; a false result sends it down the **No** path. Both paths leave the block, and you build different steps on each, so the flow does one thing when the test passes and another when it fails. You can also test several things at once: add more parts and join them with AND or OR, and use the brackets to control which parts are grouped together when they are weighed up.

## When to use it

Reach for it at any point where the flow should do one thing in one case and something else in another - a gate that lets work continue only when a record is valid, a guard that stops before a risky step, a fork that handles paid and unpaid orders differently. When you are choosing between exactly two outcomes from a single test, this is the most direct block for the job. If instead you are routing one value across many possible cases, a [Value Router](value-router.md){.fr-block} keeps that tidier than a stack of Conditions, and an [AI Router](ai-router.md){.fr-block} decides the path from natural language rather than a fixed comparison.

## Example

Suppose a flow processes an order, and an earlier step left the order details in Initial Data. You want orders over 1000 dollars to go through a manual approval step, while smaller orders are fulfilled right away. The order looks like this:

```json
{
  "id": 5821,
  "customer": "Globex",
  "amount": 1450,
  "expedited": true
}
```

Add a <span class="fr-block">Condition</span> and set its **Value to Check** to the order amount, read from Initial Data. Set **Value Data Type** to INT, since the amount is a whole number, then pick the **Operation** GREATER THAN and set the value to compare against to 1000. That is the whole test: is the amount greater than 1000?

For this order the amount is 1450, so the test is true and the flow takes the **Yes** path - where you place the manual approval step. An order with an amount of 600 would come out false and take the **No** path, where you place the steps that fulfill it straight away.

Now suppose approval should also kick in for any expedited order, whatever its size. Instead of a second <span class="fr-block">Condition</span>, add a second part to this one: keep the amount check as the first part, add a part that checks the expedited flag (**Value Data Type** BOOLEAN/CHECKBOX, **Operation** IS TRUE), and join the two parts with OR. The **Yes** path now runs whenever the amount is over 1000 or the order is expedited, and only orders that are both small and not expedited fall through to the **No** path.

## Configuration

| Field | Description |
| --- | --- |
| Value to Check | Required. The value the test runs against - usually an expression that reads from a previous block's result, Initial Data, or a Data Bucket variable. |
| Value Data Type | Required. The kind of value you are checking, such as STRING, INT, DOUBLE, BOOLEAN/CHECKBOX, DATETIME, IMAGE, or a JSON object or array. The available comparisons depend on this choice, so a number offers GREATER THAN while a checkbox offers IS TRUE. |
| Operation | Required. The comparison to run against the value, for example GREATER THAN, EQUALS, IS TRUE, or IS NOT EMPTY. Comparisons that take a second value - such as EQUALS - show a field where you supply the value to compare against. |
| Parts | Additional sub-tests added with the plus control. Each part is its own value, type, and comparison. Parts are joined with AND or OR, and brackets group parts so you control which ones are weighed together. |

## Things to watch for

- The Yes path runs when the test is true and the No path runs when it is false. Both paths leave the block; if you build steps on only one of them, the other case quietly leaves the flow with nothing to do.
- The comparisons offered depend on the Value Data Type you choose, so set the type to match the value. Checking a number as a STRING, for example, compares it character by character rather than by size, which can give a surprising answer.
- With several parts, the AND or OR connector between them can be switched, and the brackets decide which parts are grouped. With a mix of AND and OR, the grouping changes the outcome, so set the brackets deliberately rather than leaving the default.

## Related

- [Value Router](value-router.md)
- [AI Router](ai-router.md)
- expression-editor
