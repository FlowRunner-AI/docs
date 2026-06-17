<!-- GENERATED FILE - do not edit. Source: block-knowledge/value-router.yaml. Regenerate: make refgen -->
# Value Router

This block takes one value and sends the flow down a named path based on what that value is. You name the paths and tell each one which value or values it should match.

## How it works

You give the block a single value to look at - the Value to Evaluate. You then add a branch for each outcome you care about, give the branch a name, and tell it what the value has to be for that branch to win. Every branch name becomes its own output connector on the block, so you build different steps off each one. When the flow reaches the block, it checks your branches from top to bottom and leaves through the first one whose match succeeds. There is always one extra branch, Everything Else, that catches any value none of your branches claimed.

## When to use it

Reach for it when one known value decides which path the flow takes and there are several possible paths - dispatch on a product type, a status code, an order status, a category. A [Condition](condition.md){.fr-block} splits the flow into only two paths from a single test, so routing one value across four or five cases would mean stacking Conditions; one <span class="fr-block">Value Router</span> holds all of those cases in a single block and stays far easier to read. It matches values exactly, by the rules you set, so the routing is predictable and repeatable. When the path instead depends on a judgment that cannot be reduced to matching a value - the mood of a message, the intent behind a request - an [AI Router](ai-router.md){.fr-block} is the block that can read natural language and decide.

## Example

Suppose a flow processes new account applications, and the trigger left the application in Initial Data. Each application names the product the customer applied for in a ira_product_type field, and you want to send each product to its own handling steps. Here is a sample application the flow is starting with:

```json
{
  "applicationId": "APP-20517",
  "customer": "Dana Whitfield",
  "ira_product_type": "ira_cd"
}
```

Point the Value to Evaluate at that field so the block looks at the product code on each application. Then add one branch per product, each in Single Value mode, matching one exact code: a branch named Performance MMA matching `performance_mma`, a branch named Plus MMA matching `plus_mma`, and a branch named IRA CD matching `ira_cd`. Leave Everything Else for anything unexpected. The block now has four output connectors - the three you named plus Everything Else - and you build the steps for each product off its own connector.

For the application above, the value is `"ira_cd"`. The block checks the branches from top to bottom: Performance MMA does not match, Plus MMA does not match, IRA CD matches - so the flow leaves through the IRA CD connector and runs the IRA CD steps. An application carrying a code none of the three branches claim, say a discontinued `legacy_mma`, matches nothing and leaves through Everything Else, where you might log the unknown product for someone to review.

If you later add a second money-market code that should be handled exactly like `performance_mma`, you do not need a new branch. Switch that branch's Value Mode to Collection and list both codes; the branch then wins when the value equals either one.

## Configuration

| Field | Description |
| --- | --- |
| Value to Evaluate | Required. The single value the block routes on - usually an expression pointing at a field from a previous block's result or from Initial Data. |
| Branch Name | The label for a branch. Each name you add becomes a named output connector on the block, and you build the steps for that case off it. |
| Value Mode | How a branch matches the value. Single Value matches one exact value; Collection matches if the value equals any value in a list you give the branch; Range matches when the value falls between a low and a high bound, with both bounds included. |
| Branch value | What the branch matches against the value - one value in Single Value mode, a list of values in Collection mode, or a low and high bound in Range mode. |
| Everything Else | The built-in fallback branch, always present, taken when no other branch matches the value. |

## Things to watch for

- The block checks branches from top to bottom and takes the first one that matches, so if two branches could match the same value, the one higher in the list wins and the lower one is never reached. Order your branches with that in mind, and avoid overlapping matches unless you mean for the first to take priority.
- A Collection branch matches when the value equals any one of the values you listed. A Range branch matches when the value falls between the low and high bounds you set, and both of those bounds count as a match.
- Everything Else is always there and cannot be removed. Build something onto it even if you expect every value to match a named branch, so an unexpected value still has somewhere to go instead of stopping the flow.

## Related

- [AI Router](ai-router.md)
- [Condition](condition.md)
