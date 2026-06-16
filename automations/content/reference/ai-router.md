<!-- GENERATED FILE - do not edit. Source: block-knowledge/ai-router.yaml. Regenerate: make refgen -->
# AI Router

Use an AI model to classify input data into one of several named decisions, then route the flow down the matching branch. The AI analog of [Value Router](value-router.md).

## How it works

"Ask an AI to pick a label, then follow that label's path." You give it a decision request ("Determine the sentiment…"), the data to judge, and the allowed answers (Expected Decisions); it returns one, and the flow takes that branch.

## When to use it

Branch a flow on a judgment that needs an LLM (sentiment, intent, category, triage) rather than a deterministic value match.

## Configuration

| Field | Description |
| --- | --- |
| AI Model / AI API Key / AI Provider | Required. The model + key making the decision (same API Keys registry as [AI Agent](ai-agent.md)). |
| Decision Request | Required. Instruction telling the AI what to determine (recommended to start with "Determine…"). |
| Decision Data | Named inputs the AI evaluates (e.g. message <- [External Callback](external-callback.md) Data.message). |
| Expected Decisions | Required. The allowed outcomes (e.g. positive / negative / neutral). Each becomes a named output connector. "Everything Else" is the default/fallback decision. |
| Reference Result Data As |  |
| Assign to a Variable | Optionally store the chosen decision into a Data-Bucket variable. |

## Behavior

- AI selects exactly one of the Expected Decisions for the given Decision Data.
- Flow continues down the branch whose decision value was chosen.
- "Everything Else" (defaultDecision:true) is taken when none of the named decisions fit.
- Each Expected Decision is a named output connector visible on hover.

## Things to watch for

- Hover the block to reveal the NAMED output connectors (one per Expected Decision + Everything Else).
- Non-deterministic: the same input may route differently across runs.
- Needs an AI provider/model/key (here Anthropic claude-opus-4-8).

## Related

- [Value Router](value-router.md)
- [AI Agent](ai-agent.md)
- [Condition](condition.md)
- api-keys-registry
- expression-editor
