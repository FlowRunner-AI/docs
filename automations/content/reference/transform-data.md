<!-- GENERATED FILE - do not edit. Source: block-knowledge/transform-data.yaml. Regenerate: make refgen -->
# Transform Data

This block reshapes a value without writing code. You pick one operation from a built-in library, give it the inputs it asks for, and its result becomes the block's result.

## How it works

Think of it as a single ready-made data function. You choose an operation - reading a property off an object, sorting an array, merging two objects, formatting a date, doing a calculation - and the block shows the inputs that operation needs. When the flow reaches the block, it runs that one operation over those inputs and hands back the transformed value as its result. Each operation does one job, so you often place several of these blocks in a row, each taking the previous one's result a step closer to the shape you want.

## When to use it

Reach for it whenever you need to read, restructure, or compute a value between blocks and a built-in operation already covers it - pulling one field out of a response, trimming an object down to the keys you care about, building or sorting a list, comparing two values. It keeps the work visible on the canvas and spares you a code block. When the change is awkward to express as a chain of these blocks, or no operation fits, a single [Custom Cloud Code](custom-cloud-code.md){.fr-block} block is the cleaner choice instead.

## Example

Suppose an earlier [HTTP Request](http-request.md){.fr-block} block fetched a product, and you only need its id for the next step. Its result looks like this:

```json
{
  "primaryProductName": "Acme Widget",
  "sku": "AW-1024",
  "price": 19.99,
  "tags": ["featured", "new"]
}
```

Choose the Get Property Value operation. It asks for two inputs - the **Object** to read from and the **Property Name** to read. Point **Object** at the <span class="fr-block">HTTP Request</span> result and set **Property Name** to `primaryProductName`, and the block returns the single value `"Acme Widget"`. The block's result is read by later blocks through its alias, and you can also store it in a Data Bucket variable - say one named Product Name - so a step further down the flow can read it back.

Now suppose the next step needs the tags in alphabetical order. Operations do one job each, so this is a second <span class="fr-block">Transform Data</span> block rather than a setting on the first. Choose the Sort Array operation and give it the product's tags. Sorting `["featured", "new"]` returns:

```json
["featured", "new"]
```

With a longer, unsorted list the payoff is clearer - sorting `["new", "clearance", "featured"]` returns `["clearance", "featured", "new"]`. Two small blocks, each doing one operation, took the raw response and produced exactly the id and the ordered list the rest of the flow needs, with no code written.

## Configuration

| Field | Description |
| --- | --- |
| Operation | Required. The transformation to perform, chosen from the built-in library. The library covers reading and reshaping objects (for example Get Property Value, Pick, Omit), building and reshaping arrays (Create Array, Merge, Sort Array, Filter Array), comparisons and branching (If, Equals, Switch), and date, math, and text operations. |
| (operation inputs) | The inputs the chosen operation needs - they change with the operation. Get Property Value, for instance, asks for an **Object** and a **Property Name**, while Sort Array asks only for the array to sort. Each input is a value or an expression that references an earlier result. |

## Behavior

- If you turn on the option to store the result in a variable, the same value is also written to the Data Bucket variable you choose.

## Things to watch for

- Each operation has its own set of inputs, and they expect particular kinds of value. An operation that works on a list, like Sort Array, will not behave as expected if you hand it a single object or a piece of text instead of an array; check that the inputs match what the operation reads.
- An operation does exactly one job, so chains of these blocks are normal. If a transformation needs several distinct steps, place one block per step and feed each one the previous block's result, rather than trying to make a single operation do everything.

## Related

- [Set Variables](set-variables.md)
- [Custom Cloud Code](custom-cloud-code.md)
- expression-editor
