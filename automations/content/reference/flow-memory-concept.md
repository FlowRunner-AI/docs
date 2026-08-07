<!-- GENERATED FILE - do not edit. Source: block-knowledge/flow-memory-concept.yaml. Regenerate: make refgen -->
<!-- doclint: allow-unlinked: Agent Memory -->
# Agent Memory

A support chat can pick up the thread instead of asking the customer to repeat themselves, and a multi-step helper can build on a decision it made a few turns ago - once the [AI Agent](ai-agent.md){.fr-block} can remember its recent exchanges. Turning on <span class="fr-control">Messages History</span> is what gives it that memory.

## How it works

An <span class="fr-block">AI Agent</span> can carry its recent exchanges from one run to the next - but only if you ask it to. By
default it has no memory: every run starts cold, knowing only its <span class="fr-control">System Prompt</span> and the <span class="fr-control">User
Prompt</span> it was handed this run. The User Prompt is usually where the run's own data goes - the
customer's latest message, whatever is specific to this moment - and the instant the run ends, the
agent forgets all of it. That cold start is right for a step that judges one thing at a time, but no
good for a conversation, where the agent needs to remember what came before.

<span class="fr-control">Messages History</span> is what you turn on to fix that - a toggle on the <span class="fr-block">AI Agent</span> block's own config
panel, with a <span class="fr-control">Messages History Limit</span> for how many recent messages to keep. With it on, the agent
keeps a running record of its recent messages - each run's prompt and the agent's reply are added to
that record, and on the next run the agent is shown the record along with the new prompt. So it can
follow a thread: remember a name the user gave it a moment ago, build on an answer it already gave,
stop asking for something it has already been told.

![The AI Agent block's configuration panel, its header naming the block and its System and User prompts above, with the Messages History toggle switched on and the Messages History Limit field set to 15.](../images/reference/flow-memory-messages-history.png)

FlowRunner™ manages that record for you - it loads the history into the agent at the start of each
run and appends the new turn at the end, all behind the toggle. There is no result alias to read and
nothing to add to the agent's prompts; turning the toggle on is the whole job.

The record is bounded. When you turn <span class="fr-control">Messages History</span> on the limit starts at 15, and you can set it
anywhere up to 20 messages; only that many of the most recent messages are carried forward, and older
ones fall off the back. Each exchange is two messages - the prompt and the reply - so a limit of 20
keeps roughly the last ten back-and-forths.

Underneath, that history lives in Shared Memory - the flow's own key/value store that holds values
between runs - so it survives from one run to the next the same way anything in Shared Memory does.

<!-- verified 2026-07-09: Messages History Limit maximum is 20; the field's default is 15 (AI Agents with Messages History never enabled - e.g. the Retry Logic flow's agent - carry messagesHistoryLimit=15). Each run appends the user prompt + the agent reply = 2 messages. -->
<!-- doclint: no-shot: conceptual - Shared Memory / Shared Memory: Delete are named as the backing store and a consequence; they are shown on their own reference pages -->

## When to use it

Turn <span class="fr-control">Messages History</span> on when each run continues the same conversation - a chat assistant that should remember what the customer just said, a multi-step helper that refers back to an answer it gave a few turns ago. Leave it off when every run stands alone, like a classifier that rates one item at a time; carrying history it will never use only adds cost. When it is on, keep the limit only as wide as the conversation needs - every remembered message makes the prompt longer and the call dearer.

## Giving each caller their own memory

When the same flow serves many people - or many outside systems calling in - one caller's conversation could bleed into another's, because by default every run shares one memory. You keep them apart with the flow's <span class="fr-control">Memory Anchor</span>, on the <span class="fr-control">Flow Settings</span> tab - the gear tab at the top of the flow editor's right-hand panel: anchor on a value that identifies the caller, and each one gets its own separate conversation.

![The flow editor's right-hand panel open to the Flow Settings tab (the gear icon), showing the Flow Memory section: the Memory Anchor set to the path data.customerId, with a Missing Anchor Policy dropdown set to "Terminate on Memory Access" and a Memory Expiration Policy dropdown set to "Never".](../images/reference/flow-memory-settings.png)

The <span class="fr-control">Memory Anchor</span> is the value that decides which memory a run uses: runs that arrive with the same anchor value share one memory, and a different value gets its own. In the screenshot the anchor is `data.customerId`, so every run carrying the same customer id shares that customer's memory, and two customers never mix.

You set the anchor through a small <span class="fr-control">Memory Anchor Selection</span> dialog: pick an <span class="fr-control">Anchor Source</span> - where the value comes from - and give an <span class="fr-control">Anchor Property</span>, the path to the value. For a customer id carried in the flow's Initial Data, that is Initial Data with the path `data.customerId`. Left at the default source, Flow Memory, there is no split: every run shares the one memory.

Two companion settings sit beside the anchor in the same panel - a <span class="fr-control">Missing Anchor Policy</span> for when a run arrives with no anchor value (the shot shows its default, Terminate on Memory Access) and a <span class="fr-control">Memory Expiration Policy</span> for how long an idle conversation is kept (shown at its default, Never). Each opens into a set of options; choosing an anchor and pairing it with those policies is walked through end to end in [Per-User Memory](per-user-memory-concept.md).

## Example

Picture a support chat backed by an <span class="fr-block">AI Agent</span>, where each message from the customer is one run of the block. On the first run the customer writes "Hi, I'm Dana and order 10473 still has not arrived." The agent answers, and that exchange is saved to its history.

On the next run the customer writes only "So when will it get here?" - no name, no order number. With <span class="fr-control">Messages History</span> on, the agent still has the earlier turn in view: it knows the customer is Dana and the order in question is 10473, so it answers about that order without asking again. With it off, this second run would have no idea what "it" refers to and would have to ask the customer to repeat themselves.

<!-- doclint: no-shot: a two-run conversation scenario, not a UI surface; the Messages History toggle it turns on is shown under How it works -->

## Configuration

| Field | Description |
| --- | --- |
| Messages History | Turn on to give the agent memory of its earlier runs. When on, the messages from recent prior runs of this block are fed back to the model along with the new prompt, up to the limit you set (maximum 20). When off, every run starts with no memory of earlier runs. |

## Things to watch for

- The agent's memory lives in the flow's Shared Memory, so clearing that store clears the conversation too - a [Shared Memory: Delete](shared-memory-delete.md){.fr-block} with <span class="fr-control">All</span> on wipes the agent's history along with everything else, which is easy to forget when you reset a flow's store for unrelated reasons. <!-- doclint: no-shot: conceptual - Shared Memory: Delete is shown on its own reference page -->

## Related

- [AI Agent](ai-agent.md)
- [Shared Memory: Delete](shared-memory-delete.md)
- [Shared Memory: Read](shared-memory-read.md)
