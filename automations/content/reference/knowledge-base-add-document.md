<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-base-add-document.yaml. Regenerate: make refgen -->
# Knowledge Base: Add Document

This block takes a piece of text and adds it as a document to a Knowledge Base. You can attach a few labels to it so you can find or remove that document later.

## How it works

A Knowledge Base stores text in a form that later steps can search by meaning rather than by exact wording. When you hand this block some content, the Knowledge Base does not keep it as one long string: it breaks the text into smaller passages and converts each one into the numeric form a meaning-based search needs, then files those away. How it splits and converts the text is decided once on the Knowledge Base itself, not on this block - so the same Add Document block behaves consistently no matter where in the flow you place it. Alongside the text you can attach metadata: a small set of labels, like a source name or a category, that travel with the document and that you can match against later when you list or remove documents.

## When to use it

Reach for it when a flow needs to put content into a Knowledge Base on its own, without anyone uploading a file by hand. A typical case is feeding in text another block just produced - the body of a fetched web page, a support ticket, a generated summary - so it becomes searchable for later steps or for an [AI Agent](ai-agent.md){.fr-block} that answers from that Knowledge Base. It is the in-flow equivalent of dropping a file onto the Knowledge Base by hand, which means you can keep the store current automatically as new content arrives, instead of maintaining it yourself.

## Example

Suppose an earlier [HTTP Request](http-request.md){.fr-block} block fetched a help article from your support site and returned it like this:

```json
{
  "title": "Resetting your password",
  "body": "To reset your password, open Settings, choose Security, and click Reset...",
  "category": "account"
}
```

You want this article searchable so an <span class="fr-block">AI Agent</span> can answer password questions from it later. Point the block's Knowledge Base field at your support Knowledge Base, set Content to the article body from the fetch result, and give it a File Name so it is recognizable in the Knowledge Base's document list:

```text
Knowledge Base : Support Articles
Content        : {{HTTP Request Result->body}}
File Name       : Resetting your password
```

Now attach metadata so you can find or clean up this article later. Add two labels - a source and a category - using the metadata's key/value rows:

```text
source   : support-site
category : account
```

When the flow runs, the block hands the article body to the Support Articles Knowledge Base. The Knowledge Base splits it into passages, converts each into searchable form, and stores them with your two labels attached. The Knowledge Base does this work in the background, so the document shows as processing for a moment before it is finished and ready to be searched. From then on, a later [Knowledge Base: List Documents](knowledge-base-list-documents.md){.fr-block} step filtered to category equals account will return this article, and an <span class="fr-block">AI Agent</span> pointed at this Knowledge Base can draw on it when it answers.

## Configuration

| Field | Description |
| --- | --- |
| Knowledge Base | Required. Required. The Knowledge Base to add the document to. The dropdown lists your Knowledge Bases by name. |
| Content | Required. Required. The document text to add, usually an expression pointing at a previous block's result. |
| File Name | An optional name for the document, used to recognize it in the Knowledge Base's document list. |
| Metadata | Optional labels attached to the document, as key/value pairs, that later List and Delete steps can match against. You can enter them as separate Property/Value rows, or switch to passing a single object instead. Only flat key/value pairs are allowed - a value cannot be a nested object. |

## Behavior

- Adds the content to the Knowledge Base, where it is split into passages and converted into searchable form, then stored.
- The labels you attach as metadata can be matched against later by <span class="fr-block">Knowledge Base: List Documents</span> and Delete by Filter.
- Processing happens in the background, so an added document becomes searchable a moment after the block finishes, not instantly.

## Things to watch for

- Adding a document does not finish the instant the block does. The Knowledge Base processes the text in the background, so a document you just added may not be searchable or appear in a list for a short while - it shows as processing until it is ready.
- Metadata is how you find a document again. The labels you attach here are exactly what a later <span class="fr-block">Knowledge Base: List Documents</span> or Delete by Filter step matches on, so if you skip metadata you will have no way to filter for this document later.
- Metadata labels have to be flat key/value pairs. A label's value can be text or a number, but not another object nested inside it.

## Related

- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
- [AI Agent](ai-agent.md)
