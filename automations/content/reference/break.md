<!-- GENERATED FILE - do not edit. Source: block-knowledge/break.yaml. Regenerate: make refgen -->
# Break

Placed inside a loop, this block ends the loop early: when the flow reaches it, the loop stops and the flow carries on after it, leaving any not-yet-processed items untouched.

## How it works

It is the loop's exit. You put it inside a [List Iterator](list-iterator.md) or [Repeat](repeat.md) loop, usually right after a [Condition](condition.md), so that when that condition is met and the flow reaches the Break, the loop stops there instead of running through every remaining item.

## When to use it

Use it when you do not always need to finish the whole loop: stop as soon as you have found the item you were looking for, hit a situation where you should bail out, or reached a limit you set. Pair it with a Condition so the loop breaks only when you mean it to.

## Behavior

- Reaching the Break ends the enclosing loop immediately; remaining items are not processed.
- The flow continues from whatever comes after the loop.

## Things to watch for

- Break only makes sense inside a List Iterator or Repeat loop; outside a loop it has nothing to exit.
- It is almost always placed after a Condition, so the loop stops only when your test is met rather than on the first item.

## Related

- [List Iterator](list-iterator.md)
- [Repeat](repeat.md)
- [Condition](condition.md)
