<!-- GENERATED FILE - do not edit. Source: block-knowledge/break.yaml. Regenerate: make refgen -->
# Break

Placed inside a loop, this block ends the loop early: when the flow reaches it, the loop stops and the flow carries on after it, leaving any not-yet-processed items untouched.

## How it works

It is the loop's exit. You put it inside a [List Iterator](list-iterator.md){.fr-block} or [Repeat](repeat.md){.fr-block} loop, usually right after a [Condition](condition.md){.fr-block}, so that when that condition is met and the flow reaches the <span class="fr-block">Break</span>, the loop stops there instead of running through every remaining item.

## When to use it

Use it when you do not always need to finish the whole loop: stop as soon as you have found the item you were looking for, hit a situation where you should bail out, or reached a limit you set. Pair it with a <span class="fr-block">Condition</span> so the loop breaks only when you mean it to.

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
