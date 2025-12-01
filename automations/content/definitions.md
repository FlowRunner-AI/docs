---
icon: material/alphabetical-variant
---
# Terminology

This chapter defines the key terms used throughout the FlowRunner™ documentation.

## Flow Concepts

- **Flow** - A flow is an automated process that executes a series of actions based on defined logic. Flows can run autonomously or include human oversight at designated points.

- **Flow Version** - Each flow can have multiple versions. Only one version can be active at a time. To modify an active flow, clone the current version, make your changes, stop the old version, and start the new one. You cannot edit a running flow version.

- **Flow Instance** - A flow instance is a single execution of a flow version. When a flow version is in `LIVE` state, it can be instantiated. Each instance maintains its own execution context and data. Instances are created by schedules (see [Scheduled Flows](./flow-management/scheduledflows.md)), events that activate triggers, or the [Call Flow API](./flow-execution/overview.md#callflow-commandapi).

## Flow Components

- **Block** - Blocks are the building components of flows. Block types include triggers, actions, transformers, and conditions.

- **Trigger** - A trigger pauses flow execution until a specified event occurs. Examples include form submissions, API webhooks, or scheduled times. Triggers can be placed at any point in a flow.

- **Action** - An action performs a task within a flow. Actions can send emails, call APIs, generate reports, or execute custom code. Actions receive input data, process it, and pass results to subsequent blocks.

- **Transformer** - A transformer modifies data as it moves through a flow. Use transformers to extract values, convert formats, or manipulate data structures.

- **Condition** - A condition creates branching logic in a flow. The flow takes different paths based on whether the condition evaluates to true or false.

- **Groups** - Groups are container blocks that organize other blocks. FlowRunner™ supports two group types: Trigger Group (contains multiple triggers) and Action Group (contains multiple actions).

## Flow Development

- **Flow Editor** - The Flow Editor is the visual interface for building and editing flows. It provides a drag-and-drop workspace for designing automation logic.

- **Test Mode** - Test Mode runs flows with test data before deployment. Use it to validate flow logic and identify issues before activating a flow version.

## Compliance and Monitoring

- **SLA Condition** - An SLA condition defines performance benchmarks for workflows. FlowRunner™ monitors these conditions and tracks compliance.

- **Non-compliance Rules** - Non-compliance rules specify actions to take when a flow fails to meet SLA conditions. These rules automate response to performance issues.

- **SLA Configurator** - The SLA Configurator is a tool in the Flow Editor for defining SLA conditions and non-compliance rules. Use it to configure monitoring and compliance requirements for your flows.