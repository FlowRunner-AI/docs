---
icon: material/alphabetical-variant
---
# Terminology

This chapter defines the key terms used throughout the FlowRunner™ documentation.

## Flow Concepts

- **Flow** - An automated process that runs a series of blocks based on defined logic. A flow can run on its own or pause for human input at designated points. See [Flows and Instances](learn/concepts/flows-and-instances.md).

- **Flow Version** - A flow can have several versions, but only one is **LIVE** at a time. You do not edit a running version in place; you clone it, change the copy, and switch the LIVE version over.

- **Flow Instance** - A single run of a flow version. A version creates instances only while it is **LIVE**; each instance carries its own data and its own Instance ID. Instances start on a [schedule](reference/flow-scheduling-concept.md), when a [trigger](learn/concepts/triggers.md) fires, or when something calls the flow with [Call Flow](reference/call-flow.md).

## Flow Components

- **Block** - The building unit of a flow. Blocks are grouped by the kind of work they do - triggers, actions, AI steps, flow-control utilities, groups, and subflows. See [Blocks](learn/concepts/blocks.md).

- **Trigger** - How a flow reacts to an event in the outside world - a form submission, an incoming webhook, a scheduled time. A trigger either starts a new run of the flow or resumes one that was waiting. See [Triggers](learn/concepts/triggers.md).

- **Action** - A block that performs a task within a flow - calling a service, sending a message, running custom code. An action reads its input, does its work, and exposes a result that later blocks can read.

- **[Transform Data](reference/transform-data.md)** - A utility block that reshapes a value as it moves through a flow - extracting fields, converting formats, sorting or filtering a list.

- **[Condition](reference/condition.md)** - A utility block that creates branching logic: the flow takes one of two paths depending on whether its test evaluates to true or false.

- **Loops** - Container blocks that run a set of inner steps more than once. FlowRunner™ has two: a [List Iterator](reference/list-iterator.md), which runs its steps once for every item in a list, and a [Repeat](reference/repeat.md), which keeps running its steps for as long as a condition you set stays true.

- **Groups** - Container blocks that hold and run other blocks. FlowRunner™ has two: an [Actions Group](reference/actions-group.md), which runs several actions together, and a [Triggers Group](reference/triggers-group.md), which holds several triggers.

## Flow Development

- **Flow Editor** - The visual, drag-and-drop workspace where you build and edit a flow by placing blocks and wiring them together.

- **Test Mode** - Testing built into FlowRunner's Flow Editor, not a separate mode you switch into. Right where you build a flow, you run the whole flow - or a single block - with test data, to check its logic and see what it produces before you set the version **LIVE**.

## Compliance and Monitoring

- **SLA Goal** - A service-level target a flow's runs are measured against, such as "done within four hours". You set a flow's goals on its SLA Goals tab, and FlowRunner™ tracks whether each run meets them. See [Compliance and Security](platform/compliance-and-security.md).

- **SLA Calendar** - The business-hours calendar an SLA goal measures against, so "four hours" counts working hours rather than wall-clock time across nights and weekends. You manage calendars under SLA Calendars in the workspace navigation.