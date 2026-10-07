<!-- GENERATED FILE - do not edit. Source: block-knowledge/knowledge-bases-concept.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Knowledge Bases -->
# Knowledge Bases (RAG stores)

A Knowledge Base lets an [AI Agent](ai-agent.md){.fr-block} answer from your own documents instead of only from what the model was trained on. You feed it your content - a product manual, a policy handbook, your support articles - and at question time the agent can pull back the passages that match what it was asked, so its answer is grounded in your material. This retrieve-then-answer approach is the pattern commonly called RAG, short for retrieval-augmented generation.

## How it works

A Knowledge Base does three things: it stores the documents you give it, it indexes them so
their meaning can be searched, and at question time it finds the pieces most relevant to what
was asked.

The indexing is what makes a meaning-based search possible. When you add a document, FlowRunner
does not keep it as one long block of text. It breaks the document into smaller pieces, called
chunks, and turns each chunk into an embedding - a list of numbers that captures the meaning of
that piece of text. Those embeddings live in a vector store, a kind of database built to compare
meanings and return the closest matches.

So when an <span class="fr-block">AI Agent</span> asks the Knowledge Base a question, the question is turned into an embedding
too, and the store hands back the chunks whose meaning is nearest - not the ones that happen to
share the same words. That is how a Knowledge Base answers from your content: it finds what is
relevant by meaning, and the agent writes its answer from those passages.

<!-- doclint: no-shot: conceptual - how RAG storage, indexing, and retrieval work; the Knowledge Base's own surfaces (nav, setup screen) are shown in the sections below -->
<!-- doclint: allow-unlinked: Knowledge Base -->

## When to use it

Reach for a Knowledge Base when you want an <span class="fr-block">AI Agent</span> to answer from facts you supply rather than from whatever the model already knows. It keeps answers grounded in your material and lets you update what the AI knows by changing documents instead of retraining anything. The trade-off is that it is a standing resource you configure and feed - it needs its own vector store and an embedding API key from an AI provider - not a single block you drop into a flow. So it is worth setting up when an agent needs real, current domain knowledge, and overkill when a short fixed instruction in the agent's prompt would do. <!-- doclint: no-shot: conceptual guidance on when a Knowledge Base is worth it; the AI Agent that draws on it is shown on its own reference page --> <!-- doclint: allow-unlinked: Knowledge Base -->

## Creating a Knowledge Base

You create a Knowledge Base from the Knowledge Bases group in the workspace navigation,
under Agent tools & Knowledge - hover the group and click the <span class="fr-control">+</span>.

![The workspace navigation under Agent tools & Knowledge, hovering the Knowledge Bases group: a plus icon for creating a new Knowledge Base appears at the right, with MCP Servers below.](../images/reference/knowledge-bases-nav.png)

## The setup screen

Creating a Knowledge Base is a two-step dialog. The walkthrough below creates a
Knowledge Base named Product Docs - a store for a product manual an agent will answer
from - backed by Qdrant, one of the vector stores FlowRunner supports. The first step,
<span class="fr-control">General Settings</span>, decides what the Knowledge Base is and how it processes text:

- <span class="fr-control">Title</span> and <span class="fr-control">Description</span> - a name and a required summary for the Knowledge Base.
- <span class="fr-control">Embedding Model</span> - the model that turns your text into embeddings, picked from the
  supported AI providers, and an <span class="fr-control">AI API Key</span> - your own key from that provider's
  account, used whenever your text is sent to the provider to be embedded.
- <span class="fr-control">Vector Store</span> - which store holds those vectors: MongoDB Atlas, Qdrant, PostgreSQL
  with the pgvector extension, or OpenSearch. The choice is permanent - to move a Knowledge
  Base to another store, create a new one.
- <span class="fr-control">Chunk Size</span> and <span class="fr-control">Chunk Overlap</span> - how each document is sliced. Chunk Size caps how
  many characters one chunk holds; Chunk Overlap repeats the tail of one chunk at the
  start of the next, so an idea that spans the boundary is not cut in half. Larger chunks
  preserve more context per match; smaller ones make retrieval more precise.

<!-- verified in-product 2026-08-14 (Documentation Flows -> Knowledge Bases -> +): the create dialog is now a two-step wizard titled "Create AI Agents Knowledge Base" with steps "1 General Settings" / "2 Storage Configuration". Step 1 carries Title, Description (REQUIRED - inline "Description is required"), Embedding Model (default "Text Embedding 3 Small"; options grouped by provider: Open AI, Google Gemini AI, Mistral AI, Cohere, Voyage AI), AI API Key (required, "Select API Key Setup or enter new key" + Save as Setup), Vector Store (NO default; exactly MongoDB Atlas / Qdrant / PostgreSQL (pgvector) - the In-Memory adapter was removed in release 1.0.13, FR-3316), Chunk Size (2000), Chunk Overlap (300). Chunk help tooltips verbatim as in the ui block. -->
<!-- doclint: no-shot: the setup screen is shown by knowledge-bases-setup.png above; this text names the fields it depicts -->
<!-- doclint: allow-unlinked: Knowledge Base -->

![The first step of the Create AI Agents Knowledge Base dialog, General Settings: a Title of Product Docs, a Description, an Embedding Model set to Text Embedding 3 Small, an AI API Key entered, a Vector Store set to Qdrant, and Chunk Size and Chunk Overlap fields with explanatory help text. A step indicator at the top shows Storage Configuration as the second step.](../images/reference/knowledge-bases-setup.png)

## Connecting the vector store

The vector store is your own database, not something FlowRunner hosts for you. Whichever
option you pick, you bring a running instance - an Atlas cluster, a Qdrant instance, a
PostgreSQL database, or an OpenSearch cluster - and the dialog's second step, <span class="fr-control">Storage Configuration</span>, asks for
whatever the chosen store needs to connect. For the Product Docs walkthrough, that is the
Qdrant instance and the collection its vectors will live in:

- **MongoDB Atlas** - the <span class="fr-control">Connection String</span> from your Atlas dashboard (Database →
  Connect → Drivers). Press <span class="fr-control">Test</span> and the dialog connects to the cluster, then lets you
  pick the <span class="fr-control">Database Name</span> and <span class="fr-control">Collection Name</span> from what it finds there - or name
  new ones.
- **Qdrant** - the instance <span class="fr-control">URL</span> (for Qdrant Cloud, in the form
  `https://your-cluster.qdrant.io:6333`), an <span class="fr-control">API Key</span>, and the <span class="fr-control">Collection Name</span> that
  will hold the vectors.
- **PostgreSQL (pgvector)** - the <span class="fr-control">Host</span> name or IP address on its own, with no protocol
  or port; the <span class="fr-control">Port</span> (`5432` is filled in); the <span class="fr-control">Database</span>, <span class="fr-control">User</span> and <span class="fr-control">Password</span>;
  and an <span class="fr-control">SSL mode</span>. SSL mode starts at **Require**, which encrypts the connection. Choose
  **Verify full** to also check the server's certificate, or **Disable** for a local database
  without encryption. Press <span class="fr-control">Test</span>, then pick the <span class="fr-control">Table</span> - the list shows tables that
  already hold vectors - or type a new name; `knowledge_base_vectors` is filled in. The
  database needs the pgvector extension installed, or a user allowed to install it.
- **OpenSearch** - the <span class="fr-control">Node URL</span> with its protocol and port, such as `https://host:9200`,
  and a <span class="fr-control">Username</span> and <span class="fr-control">Password</span>. <span class="fr-control">Verify SSL certificate</span> is on; turn it off only for
  a cluster with a self-signed certificate. Press <span class="fr-control">Test</span>, then pick an <span class="fr-control">Index</span> or type a
  new name. The cluster needs OpenSearch 2.4 or newer with the k-NN plugin.

For every store except Qdrant, the table, collection or index picker stays locked until a
test succeeds. A failed test says why under the first field - **Could not resolve the
database host name** for a PostgreSQL host that does not exist, **Could not connect to the
cluster** for an OpenSearch node that cannot be reached.

Qdrant and PostgreSQL also offer a <span class="fr-control">Search entire collection</span> checkbox, and OpenSearch a
<span class="fr-control">Search entire index</span> checkbox when the index you pick already holds data. Left off, a
search sees only the documents added through this Knowledge Base; turned on, it searches
everything already stored in that collection, table or index.

<!-- RELEASE devtasks2 / v.1.1.3 (FR-3662 -> FR-3666), DRIVEN 2026-10-06 on dev.flowrunner.ai (create dialog, nothing created).
     The prod bundle carries the same strings ("OpenSearch Configuration", "PostgreSQL (pgvector) Configuration", "Verify SSL
     certificate", "SSL mode", "Search entire index"); WEAVIATE IS ON DEV ONLY (FR-3691, 0 hits in the prod bundle) - not
     documented. DRIVEN: Vector Store options; OpenSearch panel = Node URL (placeholder https://host:9200) + TEST, Username,
     Password, Verify SSL certificate (checked by default), Index ("Test connection first", disabled); TEST against
     https://opensearch-probe.invalid:9200 -> "Could not connect to the cluster" under Node URL. PostgreSQL panel = Host
     (placeholder db-postgresql-fra1-48213-0.b.db.example.com) + TEST, Port 5432, Database, User (placeholder postgres),
     Password (masked), SSL mode (Disable / Require / Verify full, default Require), Table (knowledge_base_vectors; the button
     is DISABLED until TEST succeeds), Search entire collection (off); TEST against pg-probe.invalid -> "Could not resolve the
     database host name". SOURCE (Sergey Androsov, FR-3666, 2026-09-30): store fixed at creation; host without protocol/port;
     table list = tables with a vector column; pgvector installed or installable (CREATE EXTENSION needed); OpenSearch 2.4+ with
     k-NN, username/password only; Search entire index only for an existing index with data. NOT DOCUMENTED (not driven, needs
     a real store): column/field pickers for an existing table/index with data; the OpenSearch < 2.12 1024-dimension limit;
     what ticking Search entire collection reveals. The 2026-10-06 gate flagged the old "embeddings produced outside FlowRunner"
     use case as an unproven compatibility promise - removed. -->

<!-- verified in-product 2026-08-14 (create dialog step 2, all three stores driven): Qdrant = URL / API Key / Collection Name / Search entire collection; MongoDB Atlas = Connection String (+ Test button; Database Name and Collection Name comboboxes stay disabled - "Test connection first" / "Select database first" - until Test succeeds); PostgreSQL = Host / Port (5432) / Database / User / Password / Table Name (placeholder knowledge_base_vectors) / Search entire collection. Tooltips captured verbatim in the ui block. MongoDB has NO Search entire collection checkbox. -->
<!-- doclint: allow-unlinked: Knowledge Base -->

![The second step of the Create AI Agents Knowledge Base dialog, Storage Configuration, with Qdrant selected: fields for the instance URL, an API Key, and a Collection Name of product-docs, plus a Search entire collection checkbox, with Back and Create buttons below.](../images/reference/knowledge-bases-storage.png)

## The Knowledge Base's own screen

Once created, Product Docs opens from the same Knowledge Bases group in the
navigation, and it has two tabs. <span class="fr-control">Setup</span> carries the choices from the create dialog.
<span class="fr-control">Data</span> lists the documents the Knowledge Base holds and shows each document's status
while it is being processed.

<!-- doclint: no-shot: MARK'S DECISION 2026-08-15 - Knowledge Bases are verified by the QA team; no recapture work needed. Tabs + editability verified 2026-07-10 on Tests workspace "Test KB" (ui block); the Product Docs Setup/Data shots and the kb-attach-to-agent.png refresh are deliberately NOT being produced. -->
<!-- doclint: allow-unlinked: Knowledge Base -->

## Giving a Knowledge Base to an agent

Creating a Knowledge Base does nothing on its own - an agent has to be pointed at it. You do that
on the <span class="fr-block">AI Agent</span> block: open <span class="fr-control">Manage Capabilities</span>, go to <span class="fr-control">Knowledge</span>, and add the Knowledge
Base from the list of the workspace's knowledge bases. Once the manual has been added -
the next section shows how, with an [Add Document](knowledge-base-add-document.md){.fr-block}
block - ask the agent a question the
manual answers, say what the warranty period is, and the reply comes from that document
instead of from general training.

<!-- verified in-product 2026-07-10 (Tests workspace, "Agent With Knowledge" flow): the AI Agent's Manage Capabilities -> Knowledge category has two groups - "Document Management" (the Add/Delete/List action tools) and "Search", which lists the workspace's knowledge bases (here "Test KB") each with a + to attach. -->
<!-- LABEL DRIFT observed 2026-08-06 (Documentation Flows, zero KBs): the groups render as "DOCUMENT MANAGEMENT ACTIONS" and "KNOWLEDGE BASES" (empty state: "There are no registered knowledge bases in the workspace. Create a new knowledge base."). Prose above deliberately describes rather than quotes the group label. MARK'S DECISION 2026-08-15: KBs are verified by the QA team - the kb-attach-to-agent.png recapture is deliberately NOT being redone; the Test KB shot stands. -->

![The Manage AI Agent Capabilities window with the Knowledge category selected. The right panel has two groups: Document Management (the Add Document, Delete Document, Delete by Filter, and List Documents action tools) and Search, which lists the workspace's knowledge bases - here "Test KB" - each with a plus button to add it to the agent.](../images/reference/kb-attach-to-agent.png)

## Loading and maintaining documents

A Knowledge Base is read at question time, but the documents have to get into it first.
For Product Docs, that is a flow with an Add Document block loading the product manual;
once the document finishes processing on the <span class="fr-control">Data</span> tab, the agent's warranty-period
answer comes from the manual instead of from general training. The same four action
blocks then keep the content current:

- [Add Document](knowledge-base-add-document.md){.fr-block} - add a document.
- [List Documents](knowledge-base-list-documents.md){.fr-block} - list what the Knowledge Base holds.
- [Delete Document](knowledge-base-delete-document.md){.fr-block} - remove one document by its file id, read from an earlier List Documents block.
- [Delete by Filter](knowledge-base-delete-by-filter.md){.fr-block} - remove several at once, filtered on the metadata you attached when adding them.

Because a flow manages the documents, the Knowledge Base can stay in sync with wherever your
content lives. A trigger block that waits for new content in another service can pass it to
Add Document, so each new piece lands in the Knowledge Base without anyone uploading it, and
Delete by Filter removes it when the source goes away.

You can also hand those same action blocks to an <span class="fr-block">AI Agent</span> as tools. Then the agent decides for
itself when to add or delete a document - saving something it was told to remember, or clearing
an entry that is out of date - instead of you wiring every change into a flow.

<!-- verified in-product 2026-07-10 (Manage AI Agent Capabilities, keyword "knowledge base"): the four Knowledge Base action blocks are attachable to an AI Agent as tools - descriptions verbatim: "Adds a document to a knowledge base for later retrieval." / "Lists documents in a knowledge base with optional metadata filter, limit, and offset." / "Deletes a specific document from a knowledge base by file ID." / "Deletes documents from a knowledge base matching a metadata filter." -->
<!-- doclint: no-shot: each Knowledge Base action block is shown on its own reference page; this section explains when to reach for them from a flow or an agent -->

## Things to watch for

- The embedding model, chunk size, chunk overlap, and vector store are chosen in the create dialog, and on a Knowledge Base that holds documents they are read-only - you cannot change how existing content was sliced or embedded after the fact. Treat them as permanent choices: to switch, you create a fresh Knowledge Base and add the documents again. The title, description, and <span class="fr-control">AI API Key</span> stay editable, so you can rename it or rotate the key at any time.
- Adding a document is not instant. In the document list on the Knowledge Base's <span class="fr-control">Data</span> tab, a new document shows as Processing while it is being chunked and embedded, and only becomes searchable once it reaches Completed. A query run right after you add will not find content that is still processing.

## Related

- [Knowledge Base: Add Document](knowledge-base-add-document.md)
- [Knowledge Base: List Documents](knowledge-base-list-documents.md)
- [Knowledge Base: Delete Document](knowledge-base-delete-document.md)
- [Knowledge Base: Delete by Filter](knowledge-base-delete-by-filter.md)
- [AI Agent](ai-agent.md)
