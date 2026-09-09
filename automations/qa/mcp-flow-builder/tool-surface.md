# Tool-surface coverage — FlowRunner MCP Flow Builder (dev), run of 2026-09-02

Generated from automations/.cache/mcp-qa/run-*.jsonl by the recorder hook. 'errors' are isError results or ERROR:/BAD_REQUEST:/… texts.

| tool | calls | errors | valid result shape (first ok) | error texts seen (distinct, truncated) |
|---|---|---|---|---|
| `readme` | 1 | 0 | text(34986 chars) |  |
| `set_context` | 2 | 0 | {draftCleared, flowId, ok, workspaceId} |  |
| `list_workspaces` | 1 | 0 | array[4] |  |
| `list_flows` | 2 | 0 | array[6] |  |
| `create_flow` | 14 | 0 | {flowId, id, name, version} |  |
| `load_flow` | 2 | 0 | {edgeCount, flowId, id, name, nodeCount, version} |  |
| `save_flow` | 20 | 0 | {elementCount, errorMessage, id, status, version} |  |
| `start_flow` | 16 | 0 | {ok, result} |  |
| `stop_flow` | 14 | 0 | {ok, result} |  |
| `set_flow_schedule` | 4 | 0 | {ok, result} |  |
| `get_flow_schedule` | 4 | 0 | {schedule} |  |
| `list_block_types` | 1 | 0 | {actions, ai, logicAndFlowControl, loopsAndGroups, timing, triggers} |  |
| `list_extension_services` | 2 | 0 | array[34] |  |
| `list_extension_methods` | 1 | 0 | array[2] |  |
| `search_extensions` | 3 | 0 | array[3] |  |
| `get_block_schema` | 27 | 0 | {blockType, connectionInfo, connections, description, fields, hasResult, inputSchema, operationDetail, operatio} |  |
| `get_service_config` | 1 | 0 | {} |  |
| `set_service_config` | 1 | 0 | {notARealField} |  |
| `list_knowledge_bases` | 1 | 0 | array[0] |  |
| `add_block` | 56 | 0 | {issues, name, nodeId, resultAlias, type} |  |
| `configure_block` | 26 | 0 | {issues, name, nodeId, resultAlias} |  |
| `wire_edge` | 38 | 0 | {fromStatus, toStatus} |  |
| `remove_edge` | 2 | 0 | {fromStatus, toStatus} |  |
| `remove_block` | 4 | 0 | {nodeCount, removed, removedChildren} |  |
| `list_condition_operators` | 2 | 0 | array[13] |  |
| `set_condition_parts` | 5 | 0 | {issues, name, nodeId, resultAlias} |  |
| `add_router_case` | 2 | 0 | {caseId, issues, name, nodeId, resultAlias} |  |
| `add_ai_router_decision` | 2 | 0 | {decisionId, issues, name, nodeId, resultAlias} |  |
| `set_data_bucket_fields` | 4 | 0 | {issues, name, nodeId, references, resultAlias} |  |
| `resolve_dictionary` | 1 | 0 | {cursor, items} |  |
| `list_connections` | 1 | 0 | {connections, count} |  |
| `set_connections` | 1 | 0 | {count, ok} |  |
| `get_connection_url` | 1 | 0 | {url} |  |
| `list_ai_providers` | 1 | 0 | array[1] |  |
| `list_ai_api_key_setups` | 1 | 0 | array[0] |  |
| `add_agent_tool` | 2 | 0 | {issues, toolId} |  |
| `remove_agent_tool` | 0 | 0 | — |  |
| `configure_agent_tool` | 1 | 0 | {issues, toolId} |  |
| `get_flow_summary` | 13 | 0 | {edges, globalIssues, nodes} |  |
| `get_node_details` | 13 | 0 | {blockType, children, connections, fields, flowElementId, groupId, id, issues, name, resultAlias, sampleResult,} |  |
| `get_flow_json` | 1 | 0 | {clientMetadata, clientTimeZone, description, elements, firstElementId, flowGroupId, flowId, groups, id, metaIn} |  |
| `test_run_block` | 2 | 0 | {completed, dataLoadedToS3, elementId, elementType, endTimeInMillis, error, executionContextId, failed, flowVer} |  |

Never called in the recorded run: `remove_agent_tool` (get_connection_url, get_service_config, set_service_config, set_connections were exercised at 03:45 UTC after this table's data was cut; see findings-log.md).
