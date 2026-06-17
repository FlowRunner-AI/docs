<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-base-add-document.yaml. Regenerate: make refgen -->
# Knowledge Base: Add Document

Programmatically add a document (content + metadata) to a Knowledge Base; it gets chunked, embedded, and stored in the KB's vector store.

## How it works

"Index this text into the knowledge base." The KB's Setup (embedding model + chunk size/overlap + vector store) governs how it's stored; metadata lets you tag it for later filtered list/delete.

## When to use it

Ingest content into a RAG store from within a flow (the flow equivalent of uploading a file on the KB Data tab).

## Configuration

| Field | Description |
| --- | --- |
| Knowledge Base | Required. Target KB (UI shows the KB name; stored as its id). |
| Content | Required. The document text to ingest (e.g. an [HTTP Request](http-request.md){.fr-block} result). |
| File Name | Optional name for the document. |
| Metadata | Tags attached to the document; used by List/Delete filters. Only flat key-value pairs are supported. Nested objects are not allowed. |

## Behavior

- Adds the content to the KB; it is chunked + embedded per the KB's AI Setup and stored in the vector store.
- Attached metadata is queryable by List/Delete-by-Filter.

## Things to watch for

- Ingestion is async (the Data tab shows Processing -> Completed).
- Metadata is what later filters (List/Delete by Filter) match on.
- Metadata must be FLAT key-value pairs — nested objects are not allowed (product tooltip).
- KB is identified by id; the UI dropdown shows the friendly name.

## Related

- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [Knowledge Bases (RAG stores)](knowledge-bases-concept.md)
- [AI Agent](ai-agent.md)
