<!-- GENERATED FILE - do not edit. Source: block-knowledge/ai-router.yaml. Regenerate: make refgen -->
# AI Router

This block hands some data to an AI model, asks it to pick one label from a list you define, and then sends the flow down the branch that matches the label it picked.

## How it works

You set up three things: an instruction telling the AI what to decide (the Decision Request, like "Determine the sentiment of the message"), the data you want it to judge (the Decision Data), and the list of labels it is allowed to choose from (the Expected Decisions, like positive, negative, and neutral). Each label you list becomes its own named output connector on the block. When the flow reaches the block, the AI reads the data, chooses exactly one of your labels, and the flow leaves through that label's connector. One label is always the fallback, named Everything Else: the AI falls back to it when none of your other labels fit the data.

## When to use it

Reach for it when the branch your flow should take depends on a judgment a human would make rather than a value you can match exactly - is this message angry or pleased, is this request a refund or a complaint, is this ticket urgent. A [Value Router](value-router.md){.fr-block} or a [Condition](condition.md){.fr-block} can split the flow when the deciding factor is a known value (status equals "cancelled", priority equals "high"), but neither can read a sentence and tell you the mood behind it. The trade-off is that the answer comes from an AI model, so it costs a model call and the same input will not always route the same way.

## Example

Suppose an [External Callback](external-callback.md){.fr-block} trigger receives an incoming support message, and you want to route it by how the customer sounds. The trigger hands you a payload like this:

```json
{
  "message": "I have been waiting three days and nobody has replied. This is unacceptable.",
  "customerId": 4821
}
```

Add an <span class="fr-block">AI Router</span>. In Decision Request, write the instruction for the AI: "Determine the sentiment of the message." In Decision Data, add one named input - call it message - and point it at the trigger's message field. In Expected Decisions, list the three labels you want to handle: positive, negative, and neutral. The block keeps a fourth label, Everything Else, as the fallback. Each of these four labels now shows up as a named output connector on the block.

On the negative connector, place a [Set Variables](set-variables.md){.fr-block} block that stores a Sentiment variable set to "negative" (and the matching value on the other two branches). When the flow runs against the message above, the AI reads it, judges the tone as angry, and chooses negative - so the flow leaves through the negative connector and runs the block that marks the message negative. A calm "Thanks, that fixed it!" would instead leave through the positive connector. Anything the AI cannot place in positive, negative, or neutral leaves through Everything Else, so the message is never stuck with nowhere to go.

## Configuration

| Field | Description |
| --- | --- |
| AI Provider | Required. Which AI service makes the decision. |
| AI Model | Required. Which model from that provider judges the data. |
| AI API Key | Required. The saved key that authorizes the model call, chosen from the same keys you register for the [AI Agent](ai-agent.md){.fr-block} block. |
| Decision Request | Required. The instruction telling the AI what to decide. Starting it with "Determine" works well, for example "Determine the sentiment of the message". |
| Decision Data | The values the AI judges. Each one has a name and an expression pointing at the data to evaluate, usually a previous block's result or a trigger's payload. |
| Expected Decisions | Required. The labels the AI is allowed to choose from. Each label becomes a named output connector on the block. One of them, Everything Else, is the fallback the AI takes when none of the others fit. |

## Things to watch for

- The named output connectors are only visible when you hover the block - one for each label in Expected Decisions, plus Everything Else. If a branch looks unwired, hover the block to find its connector.
- Because an AI makes the call, routing is not deterministic - the same input can take a different branch on a different run. Do not rely on it for decisions that must be exact and repeatable; use a <span class="fr-block">Value Router</span> or a <span class="fr-block">Condition</span> for those.
- The block needs an AI provider, model, and saved API key before it can run. Without a working key the decision cannot be made.
- Always handle the Everything Else branch. The AI sends anything it cannot place into one of your labels down this path, so leave it wired to something rather than a dead end.

## Related

- [Value Router](value-router.md)
- [AI Agent](ai-agent.md)
- [Condition](condition.md)
- api-keys-registry
- expression-editor
