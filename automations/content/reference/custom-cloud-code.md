<!-- GENERATED FILE - do not edit. Source: block-knowledge/custom-cloud-code.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Custom Cloud Code -->
# Custom Cloud Code

This block runs a snippet of JavaScript as a step in your flow. You pass values in as named arguments, write your logic, and the value you return becomes the block's result.

## How it works

Each time the flow reaches this block, your code runs once, on the server, as a single step.
Data flows in through the block's <span class="fr-control">Arguments</span> list: each argument is a name plus a value
expression that reads a previous step's result, and inside the <span class="fr-control">Open Code Editor</span> modal that
name is a ready-to-use top-level variable. The values arrive already typed as the arrays,
objects, and numbers they were upstream - nothing is stringified - so an array stays an array
you can call `.filter()` on. Whatever your code returns becomes the block's result. Data flows
back out under the alias you set in <span class="fr-control">Reference Result Data As</span>: later blocks pick that alias in
the Expression Editor and read into it, for example <span class="fr-expr">Custom Cloud Code Result → openCount</span>.

The code runs in its own isolated sandbox, created fresh on every run. Because it is a brand-new
isolate each time, nothing you set persists between runs, and that same isolation is what keeps
each run fast and predictable.

## When to use it

Reach for it, from the Actions group in the block palette, when a few lines of code would be cleaner than wiring up several blocks to do the same thing. Reshaping a payload, computing a value, or combining two blocks' outputs is often a short snippet, where the no-code equivalent might be a chain of [Transform Data](transform-data.md){.fr-block} blocks that clutters the flow. It is also how you do something genuinely custom that no built-in block offers. The one thing it is not for is reaching outside the flow: the code has no network or file access, so let blocks like [HTTP Request](http-request.md){.fr-block} and the database actions handle input and output, and use your code to work on what they return.

## Example

Suppose an upstream <span class="fr-block">HTTP Request</span> block fetched a list of orders. In the <span class="fr-control">Arguments</span> list, add one named orders whose value expression is the <span class="fr-block">HTTP Request</span> block's result, then write the code in the <span class="fr-control">Open Code Editor</span> modal to shape that array down to what the next step needs:

```javascript
// "orders" is the array returned by the HTTP Request block
const open = orders.filter(order => order.status === "open");
return {
  openCount: open.length,
  openIds: open.map(order => order.id),
};
```

![The Code Editor modal: an argument named orders bound to the HTTP Request result, alongside the code that uses it.](../images/reference/custom-cloud-code-example.png)

The block's result is the object you return, here `{ openCount, openIds }`. It is read through the alias set in <span class="fr-control">Reference Result Data As</span>, which for this block is <span class="fr-block">Custom Cloud Code</span> Result. A later step picks that alias in the Expression Editor and reads into the returned object - a [Condition](condition.md){.fr-block} might gate on <span class="fr-expr">Custom Cloud Code Result → openCount</span> > 0, or a Send Email block might list <span class="fr-expr">Custom Cloud Code Result → openIds</span> in its body - so the count and ids the code computed drive the rest of the flow.

## As an AI Agent tool

<span class="fr-block">Custom Cloud Code</span> can also be handed to an [AI Agent](ai-agent.md){.fr-block} as a tool, so the agent runs your
snippet on its own when it needs to - to do a calculation or reshape some data mid-task.
You attach it from the agent block's tools drawer.

Used this way, and only this way, its arguments gain two extra fields under
<span class="fr-control">Prepare for AI Agent</span>:

- <span class="fr-control">Value Type</span> - the data type the agent must supply, such as a string or a number.
- <span class="fr-control">Description</span> - what the argument is for, written for the agent. Together with the
  type, this is how the agent knows what to pass, and when to reach for the tool.

The value then decides who supplies each argument:

- Leave a value empty and it becomes one of the tool's parameters - the agent fills it at
  call time from the type and description.
- Set a value, static or an expression, and it is fixed input the agent cannot see or change.

As an ordinary block step, none of this appears: an argument is just a name and a value.

![The Code Editor's Arguments panel for a Custom Cloud Code tool: an argument's name and value fields above a Prepare for AI Agent section with a Value Type dropdown and a Description field that tell the agent what to pass.](../images/reference/custom-cloud-code-agent-tool.png)

## Configuration

| Field | Description |
| --- | --- |
| Arguments | The values your code can use. Each argument has a name and a value, where the value is either static or an expression that references a previous block's result. Inside the code, each argument is available as a top-level variable of the same name. |
| Code | The JavaScript to run. Press <span class="fr-control">Open Code Editor</span> to write it in the full-screen Code Editor modal, where the <span class="fr-control">Arguments</span> panel sits beside the editor. Return the value that becomes this block's result. |

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Reference Result Data As | The alias used to reference this block's result in later blocks. |
| Assign to a Variable | Optionally store the result in a Data Bucket variable too; you choose the bucket and the variable name. |
| Skip Block | When on, the block is skipped during execution and the value in Simulated Result is used as its output. |
| Logging | What to log to the Logging panel while the flow is LIVE, both on start and on completion. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Behavior

- async/await and Promises are supported; the block waits for them before capturing the result.
  ```javascript
  return await Promise.resolve({ ok: true });
  ```
- If you return a Promise, it is awaited and unwrapped automatically.
  ```javascript
  return Promise.resolve({ count: 3 });   // result is { count: 3 }
  ```
- Throwing an Error sets the block's status to Error, using the error's message.
  ```javascript
  throw new Error("orders is empty");
  ```
- Throw a real Error object, not a bare string or number; a non-Error throw still fails the block, but its message is lost.
  ```javascript
  throw "nope";   // fails the block, but the message is gone
  ```
- Arguments arrive as native, typed JavaScript values (arrays, objects, numbers, null); nothing is stringified.
  ```javascript
  return Array.isArray(orders);   // true when orders came from an array-returning block
  ```
- A floating, un-awaited promise rejection is ignored, and the block returns normally.

## Limitations

- It is a V8 sandbox (roughly ES2023), not Node. There is no require, fetch, process, Buffer, crypto, setInterval, btoa, or structuredClone.
- The server runs in UTC with the en-US locale; full ICU data is available.
- The result is serialized as JSON. Map, Set, and RegExp become empty objects; NaN and Infinity become null; and undefined, functions, and Symbols are dropped.
- Code runs in non-strict (sloppy) mode in a fresh isolate each time, so nothing persists between runs or instances.
- Execution is capped at 10 seconds. Around 400MB of allocation is fine, and deep recursion raises a RangeError.
- Return an object, not a bare scalar. `return 42` (or any bare number) fails with "Invalid status code: 42" - wrap it, for example `return { value: 42 }`.
- A value that cannot be JSON-serialized - a BigInt, or an object with a circular reference - does not error. The block reports Success but silently replaces your result with an error object like `{ message: "Do not know how to serialize a BigInt" }`, which downstream blocks then read as if it were valid. Return only JSON-serializable values.

## Related

- [AI Agent](ai-agent.md)
- [HTTP Request](http-request.md)
- [Handle Error](handle-error.md)
