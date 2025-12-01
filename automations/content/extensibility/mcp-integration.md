---
icon: material/alpha-m-circle
---

# MCP Server Integration

FlowRunner™ integrates with Model Context Protocol (MCP) servers to extend workflow capabilities. Register MCP servers to make their tools available as FlowRunner™ actions and AI Agent tools.

## What is MCP?

Model Context Protocol (MCP) is a standardized protocol for exposing tools and resources to AI systems. MCP servers provide collections of tools that can be called by AI agents or used directly in workflows.

When you register an MCP server in FlowRunner™, all server tools become available as workflow actions. Tools can be used in AI Agent configurations, tool parameters integrate with FlowRunner™'s Expression Editor, and tool results can be referenced by other blocks in the workflow.

## Accessing MCP Server Management

Open the MCP Server management screen using either method:

**Method 1: Block List Panel**  
Click the **MCP** icon next to the search bar in the Block List panel.

**Method 2: Quick Access Menu**  
Click the **QUICK ACCESS** button and select **MCP Servers**.

## Registering an MCP Server

To register a new MCP server:

1. **Enter the MCP URL**  
   Provide the publicly accessible URL for the MCP server.

2. **Configure Server Name**  
   Enter a name to identify this server in the FlowRunner™ UI. This name appears in the Block List panel.

3. **Set Server Logo**  
   Choose how the server appears visually:
   - **Avatar letters** - Auto-generated from the server URL
   - **Predefined logos** - Select from available icons
   - **Background color** - Cycle through color options to customize appearance

4. **Configure Authentication** (Optional)  
   If the MCP server requires authentication, expand the Authentication Settings section and configure:

      **Token Authentication:**

      * Custom Header Name (default: "Authorization")
      * Token value (e.g., "Bearer Token")

      **OAuth 2.0:**

      * Client ID
      * Client Secret

5. **Register the Server**  
   Click **REGISTER**. FlowRunner™ validates the server URL and authentication, then adds the server to your registered servers list.

If registration fails, verify the MCP URL is publicly accessible, authentication credentials are correct, and the server implements the MCP protocol correctly.

## Managing Registered Servers

The Registered Servers list displays all configured MCP servers. Each entry shows the server logo (icon and background color), server name, MCP URL, an EDIT button to modify server configuration, and a REMOVE button to delete the server registration.

### Editing a Server

Click **EDIT** to modify an existing server configuration. The edit screen shows all registration fields (URL, name, logo, authentication), an Available Tools section listing all tools exposed by the server with their descriptions and parameters, and buttons to reload tools, save changes, or cancel.

Use **RELOAD TOOLS** when the MCP server adds or updates tools without changing its URL.

### Removing a Server

Click **REMOVE** to delete a server registration. This removes the server from the Block List panel and makes its tools unavailable in workflows. Note that existing workflows using the server's tools will fail if executed.

Remove servers before deleting workflows that depend on them, or update workflows to remove MCP tool references.

## Using MCP Tools in Workflows

After registering an MCP server, its tools appear in the Block List panel under **MCP SERVERS**.

### Locating MCP Tools

MCP servers are listed by their configured name and logo. Expand a server to view its available tools. Each tool displays its icon (matching the server logo), tool name, description (on hover), and action count indicator.

### Adding MCP Tools to Flows

Drag any MCP tool from the Block List panel into the flow canvas. MCP tools function as standard FlowRunner™ actions. Configure tool parameters in the block settings panel, use Expression Editor for dynamic parameter values, reference tool results in subsequent blocks, and apply conditional logic based on tool outputs.

### Tool Parameters

MCP tool parameters integrate with FlowRunner™'s parameter system. All parameters support Expression Editor, parameter types follow FlowRunner™ conventions, required parameters are marked, and parameter validation follows the tool schema.

Access tool results using Expression Editor syntax:

```
${blockName.result.propertyName}
```

Tool results can be used as input for any downstream block in the workflow.

## Using MCP Tools with AI Agents

MCP tools are available as tools for AI Agent blocks. When configuring an AI Agent, open the AI Agent block settings, navigate to the Tools section, and select MCP tools from registered servers. The AI Agent can invoke these tools during execution.

AI Agents can call MCP tools based on task requirements, pass parameters to tools dynamically, process tool results, and chain multiple tool calls together.

For AI Agent configuration details, see [AI Agent documentation](../reference/ai-agent.md).

## MCP Tool Execution

When a workflow executes an MCP tool, FlowRunner™ sends a request to the MCP server with authentication credentials (if configured). Parameters are passed according to the tool schema. The server processes the request and returns results, which are made available to subsequent blocks.

Tool execution follows FlowRunner™'s standard error handling. If a tool fails, the workflow stops at that block unless error handling is configured. Error details are logged, and error handlers can catch and process failures.

See [Error Handling](../flow-editing/error-handling.md) for managing tool failures.

## Best Practices

### Server Configuration

Use descriptive server names that indicate the server's purpose. Configure authentication for production servers, test server connectivity before registering, and document which workflows depend on each MCP server.

### Tool Usage

Verify tool availability before building workflows. Use Expression Editor for dynamic tool parameters, add error handling for tool failures, and test workflows after MCP server updates.

### Maintenance

Reload tools after server updates, monitor tool execution for errors, update authentication credentials when they expire, and remove unused servers to keep the Block List clean.

## Troubleshooting

| Problem | Solutions |
|---------|-----------|
| **Server Registration Fails** - Cannot register MCP server | Verify the MCP URL is publicly accessible, check authentication credentials, confirm the server implements MCP protocol, and review server logs for connection errors. |
| **Tools Not Appearing** - Registered server shows no tools | Click RELOAD TOOLS in the server edit screen, verify the server exposes tools via MCP protocol, check server logs for tool discovery errors, or re-register the server if tools remain unavailable. |
| **Tool Execution Fails** - MCP tool fails during workflow execution | Verify tool parameters are correctly configured, check authentication credentials are valid, review tool execution logs, test the tool directly via the MCP server's interface, and add error handling to the workflow. |
| **Authentication Errors** - Authentication fails when calling tools | Verify authentication settings match server requirements, check token or OAuth credentials are current, test authentication by reloading tools, and contact the MCP server administrator for credential issues. |

## Related Documentation

- [AI Agent](../reference/ai-agent.md) - Using MCP tools with AI Agents
- [Expression Editor](../flow-editing/expressioneditor.md) - Referencing tool results
- [Error Handling](../flow-editing/error-handling.md) - Managing tool failures
- [Custom Actions](../extensibility/custom-action.md) - Alternative extensibility approach