---
icon: material/flower-tulip
---

# What is FlowRunner™?

FlowRunner™ is a visual workflow automation platform with native AI agent orchestration. Build workflows that run autonomously or incorporate human oversight at designated decision points.

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/v4T3lDDu-0A?si=zBpNWiMPHDFOi_Zq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What FlowRunner™ Does

FlowRunner™ orchestrates automated workflows that combine AI agents, human decision-making, and system integrations. Both technical and non-technical users can build workflows. Non-technical users work through the visual interface while technical users can leverage custom code and advanced integrations.

<div class="grid cards" markdown>

-   :material-robot:{ .lg .middle } Automate with AI Agents

    ---

    AI agents handle complex decision-making within your workflows, making intelligent choices based on workflow context and coordinating with other agents.

    [:octicons-arrow-right-24: Configure AI agents](reference/ai-agent.md)

-   :material-draw:{ .lg .middle } Build Visually

    ---

    Create workflows through a drag-and-drop interface without writing code. Design multi-branched flows with parallel execution and reusable components.

    [:octicons-arrow-right-24: Working with blocks](flow-editing/workingwithblocks.md)

-   :material-account-supervisor:{ .lg .middle } Add Human Oversight

    ---

    Insert human decision points at any workflow step. Contact people through email, Slack, WhatsApp, or phone with full context for informed decisions.

-   :material-sitemap:{ .lg .middle } Coordinate Multiple Agents

    ---

    Orchestrate teams of AI agents working together on complex tasks. Agents can invoke human oversight when needed and access tools through Model Context Protocol.

-   :material-shield-check:{ .lg .middle } Track Compliance

    ---

    Built-in audit trails, SLA monitoring, role-based access control, and compliance reporting ensure your workflows meet regulatory requirements.

    [:octicons-arrow-right-24: Compliance monitoring](flow-execution/compliance.md)

-   :material-api:{ .lg .middle } Bring Your Own Keys

    ---

    Use your own API keys for AI services. FlowRunner™ supports multiple AI providers, giving you flexibility and control over your AI infrastructure.

    [:octicons-arrow-right-24: Configure API keys](reference/ai-agent.md#configuring-the-ai-agent-block)

</div>

## Core Platform Capabilities

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } AI Agent Orchestration

    ---

    FlowRunner™ treats AI agents as first-class workflow components. Agents make decisions based on workflow context, coordinate with other agents, invoke human oversight when needed, and access tools through Model Context Protocol (MCP).

    [:octicons-arrow-right-24: Giving agents tools](reference/ai-agent.md#giving-your-agent-tools)

-   :material-account-question:{ .lg .middle } Human-in-Loop Workflows

    ---

    Add human oversight anywhere in your workflow. AI agents can pause execution, contact humans through their preferred channel, and resume after receiving input. Humans receive full context for decision-making.

-   :material-view-grid-plus:{ .lg .middle } Visual Workflow Building

    ---

    Design workflows through a visual interface with multi-branched flows, parallel execution, workflow groups for organization, branch synchronization, reusable SubFlows, and workflows as callable actions.

    [:octicons-arrow-right-24: Data flow in workflows](flow-editing/dataflow.md)

-   :material-file-document-check:{ .lg .middle } Compliance and Governance

    ---

    Automatic audit trail logging, SLA tracking and monitoring, role-based access control (RBAC), single sign-on (SSO) support, and built-in compliance reporting.

    [:octicons-arrow-right-24: Compliance features](flow-execution/compliance.md)

-   :material-cloud-upload:{ .lg .middle } Deployment Options

    ---

    Deploy FlowRunner™ in the cloud or self-host on your infrastructure. Both deployment models provide full feature parity with no feature degradation.

</div>

## Who Uses FlowRunner™

FlowRunner™ serves organizations that need automated workflows with AI decision-making, reliable human oversight of automated processes, compliance capabilities for regulated environments, multi-agent orchestration, and flexible workflow development approaches.

Business users and citizen developers build workflows visually without coding knowledge. Technical users and developers leverage custom code, advanced integrations, and API access for complex workflows. Hybrid teams combine both approaches, with technical and non-technical users collaborating on automation projects within the same platform.

## Development Approaches

FlowRunner™ supports multiple development methods to fit your team's skills and requirements. Build entirely through the visual interface (no-code), combine visual building with custom code (low-code), or develop workflows programmatically when needed (code-first). Choose the approach that works best for your team.

## What You'll Learn

This guide covers setting up your first workflow, configuring AI agents, adding human oversight points, managing workflow state and errors, building custom integrations, and monitoring and compliance reporting. Navigate through the chapters using the sidebar. Each section includes practical examples and code samples where applicable.

## Getting Started

Start with the [Installation Guide](#) to set up FlowRunner™, then proceed to [Building Your First Workflow](#) to create your first automation.

For technical implementation details, see the [Developer Reference](#). For visual workflow building, see [Workflow Builder Guide](#).