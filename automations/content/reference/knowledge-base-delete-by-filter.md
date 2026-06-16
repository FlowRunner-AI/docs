<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-base-delete-by-filter.yaml. Regenerate: make refgen -->
# Knowledge Base: Delete by Filter

Delete all documents in a Knowledge Base whose metadata matches a filter.

## How it works

A delete-by-query on the KB's documents, keyed on metadata.

## When to use it

Bulk-remove documents by tag (e.g. clear everything from a given source/run).

## Configuration

| Field | Description |
| --- | --- |
| Knowledge Base | Required. |
| Filter | Required. Documents whose metadata matches are deleted. Optional. Flat key-value pairs to filter documents (AND logic, exact match). Nested objects are not supported. |

## Behavior

- Deletes every document whose metadata matches the filter.

## Things to watch for

- Matches on the metadata set at Add time — tag documents you may want to bulk-delete.
- An overly broad filter can delete more than intended.

## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
