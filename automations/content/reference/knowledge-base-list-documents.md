<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-base-list-documents.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Knowledge Base: List Documents -->
# Knowledge Base: List Documents

This block reads back the documents stored in a Knowledge Base. You point it at one of your [Knowledge Bases](knowledge-bases-concept.md) and it returns the documents in it, optionally narrowed to the ones whose metadata matches values you give.

## How it works

Think of it as asking a Knowledge Base "which documents do you hold?" and getting a list back. The result is a list of documents, where every document carries its own id (its file id) plus whatever metadata was saved with it when it was added. If you leave the <span class="fr-control">Filter</span> empty you get every document; if you fill the <span class="fr-control">Filter</span> in, you get only the documents whose metadata matches. Because the list can be long, you read it in pages: <span class="fr-control">Limit</span> sets how many documents come back at once, and <span class="fr-control">Offset</span> sets how far into the full list that page starts.

## When to use it

Reach for it - it sits in the Actions palette, in the Knowledge Base group - whenever a flow needs to see what is actually in a Knowledge Base rather than only add to it. Two cases come up most. First, taking stock - confirming a document was added, or counting how many documents match a category. Second, and more common, getting the file id of a document so a later step can act on it: the only way to delete a specific document is to hand its file id to a [Knowledge Base: Delete Document](knowledge-base-delete-document.md){.fr-block} block, and this block is how you obtain that id. If you already know the exact document you want and have its id from somewhere else, you do not need this block at all.

## Example

Suppose you keep a Knowledge Base called Support Articles, and each article was added with metadata recording the product area it belongs to and whether it is still current. You want to clean out the retired billing articles. The first step is to find them, so you add a <span class="fr-block">Knowledge Base: List Documents</span> block, pick Support Articles in its <span class="fr-control">Knowledge Base ID</span> field, and set the <span class="fr-control">Filter</span> to match the documents you care about:

```json
{
  "area": "billing",
  "status": "retired"
}
```

![The Knowledge Base: List Documents block selected on the canvas with its configuration panel: Knowledge Base ID is Support Articles, and two Filter rows read area = billing and status = retired, with Limit and Offset left empty.](../images/reference/knowledge-base-list-documents-config.png)

The <span class="fr-control">Filter</span> matches on every pair you give and only on exact values, so this returns the documents whose metadata has both area equal to billing and status equal to retired, and no others. The exact, flat-only match is deliberate: the metadata you save with a document is a plain set of key-value labels, so the filter compares label against label rather than running a search, which is why a partial value or a nested object will not match. The block hands back a list of those documents. A trimmed view of the result looks like this:

```json
{
  "files": [
    { "fileId": "a17c-9f20", "metadata": { "area": "billing", "status": "retired" } },
    { "fileId": "b48e-1c03", "metadata": { "area": "billing", "status": "retired" } }
  ]
}
```

Each entry is one document, and the part you usually want is its fileId. The block exposes this result under the alias in its <span class="fr-control">Reference Result Data As</span> field - by default <span class="fr-expr">Knowledge Base: List Documents Result</span> - so a later block reads it through the Expression Editor under Block Data. To remove the first match, you feed that document's file id into a <span class="fr-block">Knowledge Base: Delete Document</span> block, building the reference <span class="fr-expr">Knowledge Base: List Documents Result → files[0].fileId</span> in its file-id field - the ``files`` list, index ``0``, the ``fileId`` of that entry. To delete every match rather than one, place the <span class="fr-block">Knowledge Base: Delete Document</span> inside a [List Iterator](list-iterator.md){.fr-block} pointed at <span class="fr-expr">Knowledge Base: List Documents Result → files</span>; each pass exposes one document as <span class="fr-expr">Current Iteration Item</span>, and you read its id with <span class="fr-expr">Current Iteration Item → fileId</span>, deleting the whole retired-billing set in a single walk.

## Configuration

| Field | Description |
| --- | --- |
| Knowledge Base ID | Required. The Knowledge Base to read documents from, set by its name or an expression. |
| Filter | Optional. Metadata values a document must match to be included. Each row is a property name and the value it must equal; give several rows and a document has to match all of them. Matching is exact, and only flat values are compared, so nested objects are not supported. Leave the Filter empty to return every document. |
| Limit | How many documents to return at most. Use it with Offset to read a long list one page at a time. |
| Offset | How far into the full list to start, counting from 0. With Limit, this is how you step through the documents a page at a time - for example, Offset 50 with Limit 50 returns the second page. |

**Common settings** (available on most blocks):

| Field | Description |
| --- | --- |
| Name | A label for this block on the canvas. |
| Reference Result Data As | The alias used to reference this block's result in later blocks. |
| Assign to a Variable | Optionally store the result in a Data Bucket variable too; you choose the bucket and the variable name. |
| Logging | What to log to the Logging panel while the flow is LIVE, both on start and on completion. |
| Notes | Freeform notes for documenting the block; they do not affect execution. |

## Things to watch for

- The result is a list of documents under files, not a bare array of ids. To act on a single document, read its file id from the entry you want through the result alias - for example <span class="fr-expr">Knowledge Base: List Documents Result → files[0].fileId</span> for the entry at index 0.
- An empty <span class="fr-control">Filter</span> returns every document, bounded only by <span class="fr-control">Limit</span> and <span class="fr-control">Offset</span>. If you meant to narrow the results, make sure the <span class="fr-control">Filter</span> is actually filled in.
- The <span class="fr-control">Filter</span> compares exact values and matches every pair you give, so a document is only returned when all of its metadata values match exactly. A near match or a partial value will not be found, and the comparison only looks at flat values - it cannot reach into a nested object.
- <span class="fr-control">Limit</span> and <span class="fr-control">Offset</span> cap how many documents come back in one call. If a Knowledge Base holds more documents than your <span class="fr-control">Limit</span>, raise the <span class="fr-control">Limit</span> or read further pages with <span class="fr-control">Offset</span>, or you will miss the rest.

## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
- [List Iterator](list-iterator.md)
