<!-- GENERATED FILE - do not edit. Source: block-knowledge/break.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Break -->
# Break

Placed inside a loop, this block ends the loop early: when the flow reaches it, the loop stops and the flow carries on after it, leaving any not-yet-processed items untouched.

## How it works

Think of it as the loop's early exit. You rarely want every iteration once you have found what
you came for, so you fire the <span class="fr-block">Break</span> the moment you have it - which is why it almost always sits
behind a [Condition](condition.md){.fr-block} that decides when "done enough" is true. Reaching it drops you out of the
loop and on to whatever follows.

<span class="fr-block">Break</span> breaks the loop it sits inside - the nearest enclosing one. If you have nested loops, it
ends only the inner loop and the outer loop keeps going, because the block belongs to whichever
loop currently surrounds it. It hands nothing back either: there is no result to read after a
<span class="fr-block">Break</span>, so nothing downstream references it - its whole job is to change where the flow goes
next, not to produce a value. You will find <span class="fr-block">Break</span> in the palette's Utils group.

## When to use it

Use it when you do not always need to finish the whole loop: stop as soon as you have found the item you were looking for, hit a situation where you should bail out, or reached a limit you set. Pair it with a <span class="fr-block">Condition</span> so the loop breaks only when you mean it to.

## Example

<span class="fr-block">Break</span> lives inside a [List Iterator](list-iterator.md){.fr-block} or [Repeat](repeat.md){.fr-block} loop, usually right after a <span class="fr-block">Condition</span>: when the flow reaches it, the loop stops. The block itself has almost nothing to configure - just a <span class="fr-control">Name</span> for the canvas and optional <span class="fr-control">Notes</span>. It exposes no result, so unlike most blocks there is no output alias to read afterwards; the screenshot below shows the whole panel:

![The Break block selected inside a Repeat loop's body (the canvas header reads Block "Repeat"), wired on the Yes path of a Condition that follows a Set Variables step, with its configuration panel - which holds only a Name and Notes, since Break ends the surrounding loop the moment the flow reaches it and exposes no result.](../images/reference/break-config.png)

## Configuration

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Behavior

- Reaching the <span class="fr-block">Break</span> ends the enclosing loop immediately; remaining items are not processed.
- The flow continues from whatever comes after the loop.

## Things to watch for

- <span class="fr-block">Break</span> only makes sense inside a <span class="fr-block">List Iterator</span> or <span class="fr-block">Repeat</span> loop; outside a loop it has nothing to exit.
- It is almost always placed after a <span class="fr-block">Condition</span>, so the loop stops only when your test is met rather than on the first item.

## Related

- [List Iterator](list-iterator.md)
- [Repeat](repeat.md)
- [Condition](condition.md)
