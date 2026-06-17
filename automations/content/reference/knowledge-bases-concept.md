<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-bases-concept.yaml. Regenerate: make refgen -->
# Knowledge Bases (RAG stores)

A Knowledge Base is a searchable store of your own documents that an [AI Agent](ai-agent.md){.fr-block} can draw on to answer questions. You add documents to it, and the AI can later pull back the passages that match what it was asked.

## How it works

A Knowledge Base is a place you put documents so an AI can find the parts that matter. When you add a document, FlowRunner does not store it as one long block of text. It breaks the document into smaller pieces, called chunks, and turns each chunk into an embedding - a list of numbers that captures the meaning of that piece of text. Those embeddings live in a vector store, which is built to compare meanings and return the closest matches. So when an <span class="fr-block">AI Agent</span> asks the Knowledge Base a question, the question is turned into an embedding too, and the store hands back the chunks whose meaning is nearest. That is how a Knowledge Base answers from your content instead of from the model's general training.
You set this up in two parts. The Setup tab is the configuration: a title and description, an Embedding Model that decides how text becomes numbers, the chunk size and overlap that decide how documents are sliced, and the vector store where the embeddings are kept. The Data tab is the content: the documents themselves, which you add, rename, and remove there.

## When to use it

Reach for a Knowledge Base when you want an <span class="fr-block">AI Agent</span> to answer from facts you supply - a product manual, a policy handbook, a set of support articles - rather than from whatever the model already knows. It keeps answers grounded in your material and lets you update what the AI knows by changing documents instead of retraining anything. The trade-off is that it is a standing resource you configure and feed, not a single block you drop into a flow, so it is worth setting up when an agent needs real, current domain knowledge, and overkill when a short fixed instruction in the agent's prompt would do.

## Behavior

- An <span class="fr-block">AI Agent</span> draws on a Knowledge Base by attaching it as a capability, and a flow can add, list, or remove documents using the Knowledge Base action blocks.

## Things to watch for

- The embedding model, chunk size, chunk overlap, and vector store are set when you create the Knowledge Base and lock once it holds any documents. You cannot change how existing content was sliced or embedded after the fact, so choose these with care up front - to switch, you create a fresh Knowledge Base and add the documents again. The title, description, and API Key stay editable, so you can rename it or rotate the key at any time.
- The In Memory vector store is meant for testing only. Anything you add to it is kept for about six hours and then dropped, and that window cannot be extended. For content that has to stick around, pick a vector store that persists.
- Adding a document is not instant. A new document shows as Processing while it is being chunked and embedded, and only becomes searchable once it reaches Completed. A query run right after you add will not find content that is still processing.

## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [AI Agent](ai-agent.md)
- api-keys-registry
