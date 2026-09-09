---
icon: material/flower-tulip
---
# What is FlowRunner?

The world is moving to AI agents, and you can create one almost anywhere - in your own Claude or ChatGPT account, inside the tools you already run like Intuit's QuickBooks, in nearly every app racing to add them. Before long everyone will have their own agents, and a single team will run hundreds.

That is where it turns into chaos: agents spun up all over the place, each acting on its own, with no single place to run them, connect them, keep a person in the loop, or account for what they did.

**FlowRunner is where you bring that under control.** It is a platform to configure, run, and orchestrate AI agents - your own and the ones your tools hand you - inside processes you can see end to end, wire to real services, pause for a person when a decision carries weight, and audit once they are done. The agents do the thinking; FlowRunner gives them somewhere to run, tools to reach for, and someone to answer to.

You build that orchestration as **flows**. Here is one that runs on its own - it sorts incoming form submissions, using an [AI Router](reference/ai-router.md){.fr-block} to read each request and route it to the right team: Billing, Engineering, or a general inbox.

![A flow on the FlowRunner canvas: a Form Submitted Trigger feeds a Submission Intent AI Router that branches three ways - Billing to a Submit Inquiry to Billing Dept step, Technical to Route to Engineering via Slack, and Everything Else to Send a General Inquiry Email through Gmail.](images/welcome/welcome-flow.png)

## What is a flow?
<!-- doclint: no-shot: overview section; the hero above shows a real flow, and Blocks carries the detailed shots -->

A flow is a business process laid out as steps, and each step is a block with one job. An [HTTP Request](reference/http-request.md){.fr-block} calls a service; a [Transform Data](reference/transform-data.md){.fr-block} reshapes a value; a [Condition](reference/condition.md){.fr-block} asks a yes-or-no question and forks the flow two ways; a [List Iterator](reference/list-iterator.md){.fr-block} runs a set of steps over every item in a list. You add blocks from a wide palette and connect them, and the wiring is rarely a straight line: it branches, loops, runs steps in parallel, and rejoins.

Alongside the built-in blocks, a large library of connectors for outside services - Airtable, Stripe, Slack, and many more - is there with nothing to install. Your own flows appear as blocks too, so you build a piece once and call it from anywhere. [Blocks](learn/concepts/blocks.md) covers the block library and how one block's result feeds the next.

## How a flow runs

A flow starts when something sets it off, and the data it begins with is its **Initial Data** - the form submission, the API payload, the record that triggered the run. From there the blocks run in the order you wired them. Each block produces a **result**, and that result does not disappear when the block finishes: it joins a growing pool of values the run carries - every result so far, the Initial Data, and any shared memory - that any later block can read through the [Expression Editor](learn/concepts/expressions.md).

Every run is an **instance** of the flow: its own execution, with its own data, independent of every other run. If fifty tickets arrive at once, fifty instances run side by side, each handling its own ticket. You test a flow before it goes live, watch its instances as they run, and open any one to see the exact path it took and the data it carried. [Flows and Instances](learn/concepts/flows-and-instances.md) goes into this.

## Agents and people, inside the flow
<!-- doclint: no-shot: conceptual; the agent-and-human shape is pictured in the hero above, with detail on the AI in Flows and callback pages -->

Say a flow handles an incoming support ticket. An [AI Agent](reference/ai-agent.md){.fr-block} reads the ticket and drafts a reply, drawing on a knowledge base of your own help articles to get the details right. Because the reply is going to a customer, the flow does not send it straight away - it pauses and waits for a support lead. If the lead approves, the flow sends the reply and closes the ticket; if it needs work, the agent revises and the lead takes another look.

That flow leans on two capabilities worth understanding early:

- An **AI agent** is a block you can give tools - your other flows, a knowledge base of your content, the blocks around it - and memory that carries from one run to the next, so it works with the full context of the flow. [AI in Flows](build/ai-in-flows.md) covers building with agents.
- A flow can **wait for a person**. At a step that needs human judgment it pauses, reaches the right person, and picks up where it left off when they answer. [Waiting on an External System](build/flow-control/external-callbacks.md) covers how a flow pauses and resumes.

Everything either kind of block does is recorded, so a finished instance is a record you can review and audit.

## The flexibility to model any process
<!-- doclint: no-shot: differentiators overview; each capability is deep-linked to the block reference that shows it -->

Real processes are not tidy, and a flow does not force them to be. A handful of capabilities let a flow match the shape of the work, however involved it gets.

- **Start with any block.** A flow does not have to begin with a trigger. Any block can be its first step - a plain action you run on demand, a scheduled job, a form, an incoming API call - and the data it starts with arrives as its Initial Data. You are never forced to model a process around one kind of starting event.
- **Branch as wide as the decision.** A [Condition](reference/condition.md){.fr-block} forks the flow two ways; a [Value Router](reference/value-router.md){.fr-block} sends a value down one of many named paths; an [AI Router](reference/ai-router.md){.fr-block} reads a message in plain language and picks the path itself. Branches nest and loop, so the flow follows the real decision tree, however many ways it forks.
- **Run in parallel, then regroup.** Fan a flow out into branches that run at the same time - three service calls that do not depend on each other, say - and bring them back together with a [Synchronize](reference/synchronize.md){.fr-block} block that waits for all of them before the flow moves on. A Max Waiting Time keeps one stuck branch from holding the flow forever.
- **Pause for as long as it takes.** A flow can stop mid-run and wait on the outside world - a customer to approve a quote, a payment to clear, a document to finish - and resume the instant that answer arrives, exactly where it left off. The wait is long-lived: a run can hold for up to a year (30 days on the Growth plan), so "wait for a human" can mean minutes or months.
- **Bring in any service through MCP.** Register a Model Context Protocol server once, and its whole catalog of tools becomes blocks you drop into flows and tools your agents can call on their own - no building, no hosting, no glue code.

## Build with no code, or with code
<!-- doclint: no-shot: short conceptual section; the Custom Cloud Code shots live on its reference page -->

Most of a flow you build without writing anything - add blocks, fill in their fields, wire the path. Where a step needs more than the blocks provide, a [Custom Cloud Code](reference/custom-cloud-code.md){.fr-block} block runs code you write, and you can package your own blocks as [custom extensions](extend/index.md) that appear in the palette with the rest. A single flow can mix both freely.

## Start here

- **New to FlowRunner** - the [Quick Start](learn/quickstart.md) builds your first flow end to end.
- **The core ideas** - [Core Concepts](learn/concepts/flows-and-instances.md) covers flows and instances, blocks, triggers, variables, expressions, subflows, and shared memory.
- **Building** - the [visual editor](build/flow-editor.md) is where you assemble a flow, and the Build guides go deep on data, control flow, AI, and integrations.
- **Every block** - the [Block Reference](reference/ai-agent.md) documents each block you can place, one page each.
