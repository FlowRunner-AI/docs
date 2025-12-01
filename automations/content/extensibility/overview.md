---
icon: material/alpha-e-circle-outline
---
# About Extensibility

You can extend FlowRunner™ to meet specific workflow requirements. Use MCP server integration for external tools, build custom actions for specialized operations, or create custom triggers for application-specific events.

!!! info "Pre-built Extensions"
    FlowRunner™ includes pre-built extensions for popular services including Gmail, Google Drive, Google Sheets, Outlook, Airtable, Slack, and others. Each extension provides specialized actions and triggers for that service. These extensions are built using the same extensibility framework documented in this section.

    Community developers can create and publish additional extensions to the FlowRunner™ integration directory. Approved extensions become available to all users.

## Extension Methods

FlowRunner™ supports three approaches to extensibility:

### MCP Server Integration

Register Model Context Protocol (MCP) servers to add external tools to FlowRunner™. MCP integration provides access to tools from any MCP-compatible server with automatic tool discovery and registration. Tools become available as workflow actions and AI Agent tools without requiring custom code.

MCP integration works with publicly accessible MCP servers. Register a server once, and all its tools become available across your workflows. See [MCP Server Integration](mcp-server-integration.md) for registration and usage details.

### Custom Actions

Custom Actions define new operations that function like built-in FlowRunner™ actions. Build Custom Actions when you need to integrate with third-party APIs or external services, execute complex business logic specific to your application, create reusable operations across multiple workflows, or encapsulate domain-specific functionality.

Custom Actions can be built using AI coding assistant or JavaScript (Node.js). Once developed, these actions appear in the Block List panel and can be added to any flow.

### Custom Triggers

Custom Triggers define events or conditions that pause workflow execution until activated. Unlike standard triggers that only start workflows, Custom Triggers can be placed anywhere in a flow. Use Custom Triggers to trigger workflows based on external events (webhooks, system events), pause and resume workflows at specific points, handle application-specific events tied to your business logic, or wait for user actions or external system state changes.

Custom Triggers can be reused across multiple workflows and placed at any execution point where conditional pausing is needed.

## Choosing an Extension Method

Select the appropriate extension method based on your requirements:

**Use MCP Server Integration when:**

- Tools already exist on an MCP server
- You need to integrate external services that provide MCP endpoints
- You want to leverage the MCP ecosystem without writing code
- Multiple workflows need access to the same external tools

**Use Custom Actions when:**

- You need application-specific business logic
- Integration requires custom authentication or data transformation
- Functionality is specific to your FlowRunner™ instance
- You want to create proprietary operations

**Use Custom Triggers when:**

- Workflows must pause for external events
- You need conditional execution based on application state
- Standard triggers don't match your event model
- User interaction or approval is required mid-workflow

## Extension Development

This section provides comprehensive documentation for building custom extensions. Topics include custom actions (defining new operations with configurable parameters), service configuration (adding authentication and connection settings), OAuth2 authorization (implementing OAuth2 flows for third-party services), no-code development (building actions using Codeless), JavaScript development (building actions using Node.js), dictionary operations (creating actions with dynamic parameter options), and parameter rendering (configuring how parameters appear in the UI).

Start with the appropriate development guide based on your preferred approach (Codeless or JavaScript) and the complexity of your custom extension.