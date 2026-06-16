<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-bases-concept.yaml. Regenerate: make refgen -->
# Knowledge Bases (RAG stores)

A Knowledge Base is a RAG (retrieval-augmented generation) store: documents are chunked, embedded, and stored in a vector store so AI Agents (and the KB action blocks) can retrieve relevant content by similarity.

## How it works

Title + Description (identity) → AI Setup (which embedding model + chunking turns text into vectors) → Vector Store (where the vectors live). Documents on the Data tab are processed (chunk → embed → store) asynchronously.

## When to use it

Give an [AI Agent](ai-agent.md) domain knowledge to ground its answers, or build a searchable corpus the flow can add to / query / clean up via the Knowledge Base action blocks.

## Behavior

- Documents are chunked (Chunk Size/Overlap), embedded (Provider/Model), and stored in the Vector Store.
- AI Agents attach a KB via Manage Capabilities → Knowledge; KB blocks add/list/delete documents.

## Things to watch for

- Embedding Provider/Model + Chunk Size/Overlap + Vector Store are CONFIGURABLE AT CREATION (Create dialog), then become READ-ONLY once data has been added to the KB — you can't re-chunk/re-embed documents already in the store. (On the Test KB, which had data, these showed readOnly while Title/Description/API Key stayed editable.)
- In-Memory vector store is for testing only — 6h data lifetime, non-extendable.
- Document ingestion is async (Processing → Completed) — added docs aren't queryable instantly.

## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [AI Agent](ai-agent.md)
- api-keys-registry
