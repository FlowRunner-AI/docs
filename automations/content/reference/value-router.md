<!-- GENERATED FILE - do not edit. Source: block-knowledge/value-router.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Value Router -->
# Value Router

This block takes one value and sends the flow down a named path based on what that value is. You name the paths and tell each one which value or values it should match.

## How it works

You give the block a single value to look at - the <span class="fr-control">Value to Evaluate</span>. You then add a branch
for each outcome you care about, give the branch a name, and tell it what the value has to be
for that branch to win. Every branch name becomes its own output connector on the block, so
you build different steps off each one. When the flow reaches the block, it checks your branches
from top to bottom and leaves through the first one whose match succeeds. There is always one
extra branch, <span class="fr-control">Everything Else</span>, that catches any value none of your branches claimed.

![The Value Router block selected, with its branches defined in the properties panel: Value to Evaluate reads the ticket's category from Initial Data, and three branches - Billing, Technical, and Sales - each use Single Value mode to match one exact category (billing, technical, sales).](../images/reference/value-router-config.png)

How a branch decides it matches is its <span class="fr-control">Value Mode</span>, and there are five to pick from:

- <span class="fr-control">Single Value</span> - the branch wins when the value equals one exact value you give it.
- <span class="fr-control">Single List</span> - you point the branch at a list (built by a transformer, carried on a trigger event, or returned by an earlier block), and it wins when the value equals any item in that list.
- <span class="fr-control">Collection of Values</span> - you type several values by hand, and the branch wins when the value equals any one of them.
- <span class="fr-control">Range of Values</span> - you set a low and a high bound, and the branch wins when the value falls between them, both bounds included.
- <span class="fr-control">Quick Range</span> - the same list-or-range idea written as a shorthand in square brackets: commas separate individual values and a dash marks a range, as in `[1,2,5,7]` or `[1-5]`; text values go in quotes, like `["January","March"]`.

You act on a <span class="fr-block">Value Router</span> by building different steps off each connector, not by reading a value
afterward - the routing is what the block does. It still stores the value it routed on under the
alias <span class="fr-expr">Value Router Result</span>, which a later step can reference if it needs that value, but most
flows never read it back.

## When to use it

Reach for it when one known value decides which path the flow takes and there are several possible paths - dispatch on a product type, a status code, an order status, a category. A [Condition](condition.md){.fr-block} splits the flow into only two paths from a single test, so routing one value across four or five cases would mean stacking Conditions; one <span class="fr-block">Value Router</span> holds all of those cases in a single block and stays far easier to read. It matches values exactly, by the rules you set, so the routing is predictable and repeatable. When the path instead depends on a judgment that cannot be reduced to matching a value - the mood of a message, the intent behind a request - an [AI Router](ai-router.md){.fr-block} is the block that can read natural language and decide.

## Example

Suppose a flow handles incoming support tickets, and each run starts with one ticket in Initial Data. Every ticket carries a category, and you want to send each ticket to the team that handles it. Here is a sample ticket the flow is starting with:

```json
{
  "ticketId": "T-4821",
  "subject": "I was charged twice this month",
  "category": "billing"
}
```

Point the <span class="fr-control">Value to Evaluate</span> at that category so the block routes on it. Then add one branch per team, each in <span class="fr-control">Single Value</span> mode matching one exact category: a branch named Billing matching `billing`, a branch named Technical matching `technical`, and a branch named Sales matching `sales`. Leave <span class="fr-control">Everything Else</span> for a ticket whose category is blank or unrecognized. The block now has four output connectors - the three you named plus <span class="fr-control">Everything Else</span> - and you build each team's steps off its own connector.

For the ticket above, the category is `"billing"`. The block checks the branches from top to bottom: Billing matches - so the flow leaves through the Billing connector and runs the billing steps. A ticket whose category none of the three branches claim, say a blank value or a typo, matches nothing and leaves through <span class="fr-control">Everything Else</span>, where you might drop it into a general triage queue for someone to sort.

If refunds should later be handled by the same team as billing, you do not need a new branch. Switch the Billing branch's <span class="fr-control">Value Mode</span> to <span class="fr-control">Collection of Values</span> and list both `billing` and `refund`; the branch then wins when the category is either one.

## Configuration

| Field | Description |
| --- | --- |
| Value to Evaluate | Required. The single value the block routes on - usually an expression pointing at a field from a previous block's result or from Initial Data. |
| Branch Name | The label for a branch. Each name you add becomes a named output connector on the block, and you build the steps for that case off it. |
| Value Mode | How a branch matches the value. Five modes: <span class="fr-control">Single Value</span> matches one exact value; <span class="fr-control">Single List</span> matches if the value equals any item in a list the branch points at (a list from a transformer, a trigger event, or an earlier result); <span class="fr-control">Collection of Values</span> matches if the value equals any of several values you list by hand; <span class="fr-control">Range of Values</span> matches when the value falls between a low and a high bound, both included; <span class="fr-control">Quick Range</span> is that list-or-range in a bracketed shorthand, like `[1,2,5,7]` or `[1-5]`. |
| Branch value | What the branch matches against the value - one value in <span class="fr-control">Single Value</span> mode, a reference to a list in <span class="fr-control">Single List</span> mode, several values you enter in <span class="fr-control">Collection of Values</span> mode, a low and high bound in <span class="fr-control">Range of Values</span> mode, or a bracketed shorthand in <span class="fr-control">Quick Range</span> mode. |
| Everything Else | The built-in fallback branch, always present, taken when no other branch matches the value. |

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Reference Result Data As | The alias used to reference this block's result in later blocks. |
| Logging | What to log to the Logging panel while the flow is LIVE, both on start and on completion. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Things to watch for

- The block checks branches from top to bottom and takes the first one that matches, so if two branches could match the same value, the one higher in the list wins and the lower one is never reached. Order your branches with that in mind, and avoid overlapping matches unless you mean for the first to take priority.
- A <span class="fr-control">Collection of Values</span> branch matches when the value equals any one of the values you listed. A <span class="fr-control">Range of Values</span> branch matches when the value falls between the low and high bounds you set, and both of those bounds count as a match.
- <span class="fr-control">Everything Else</span> is always there and cannot be removed. Build something onto it even if you expect every value to match a named branch, so an unexpected value still has somewhere to go instead of stopping the flow.

## Related

- [AI Router](ai-router.md)
- [Condition](condition.md)
