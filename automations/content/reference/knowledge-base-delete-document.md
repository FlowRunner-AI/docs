<!-- GENERATED FILE — do not edit. Source: block-knowledge/knowledge-base-delete-document.yaml. Regenerate: make refgen -->
# Knowledge Base: Delete Document

Delete a single document from a Knowledge Base by its fileId.
## How it works

A delete-by-id on the KB's documents.
## When to use it

Remove a specific document (typically a fileId obtained from List Documents).
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Knowledge Base | dropdown (knowledgeBaseId) | Yes |  |
| File Id | expression (string) | Yes | The document id (e.g. List Documents Result.files[0].fileId). |
## Behavior

- Removes the document with the given fileId from the KB.
## Things to watch for

- Needs the exact fileId (get it from List Documents).
## Related

- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
