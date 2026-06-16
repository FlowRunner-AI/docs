<!-- GENERATED FILE — do not edit. Source: block-knowledge/knowledge-base-list-documents.yaml. Regenerate: make refgen -->
# Knowledge Base: List Documents

List the documents in a Knowledge Base, optionally filtered by metadata, with pagination.
## How it works

A query over the KB's documents. Returns files[] (each with a fileId + metadata).
## When to use it

Enumerate/inspect KB contents, or get document ids (fileId) to delete specific docs.
## Configuration

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| Knowledge Base | dropdown (knowledgeBaseId) | Yes |  |
| Filter | repeatable Property+Value (metadata) |  | Match documents by metadata (empty = all). — Optional. Flat key-value pairs to filter documents (AND logic, exact match). Nested objects are not supported. |
| Limit / Offset | numbers (INT) |  | Pagination. |
## Behavior

- Returns the KB's documents matching the metadata filter, paginated by limit/offset.
## Things to watch for

- Result shape: files[].fileId (used by Delete Document).
- Empty filter lists all (within limit/offset).
- Filter uses AND logic + exact match on flat key-value pairs (product tooltip); nested objects unsupported.
## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
