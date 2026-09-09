| # | tool | ok | error= | shape= | issues= | status= | live (truncated) |
|---|---|---|---|---|---|---|---|
| 9 | create_flow | ✅ | true | true | true | true | { "id": "28CC5C2D-9224-4333-AEC9-39A3CB5FE757", "flowId": "F7EC1DA4-74BF-47F1-9A02-64F80818E0C6", "version": 1, "name": "MCP Probe – |
| 10 | get_block_schema | ✅ | true | true | true | true | { "type": "data-transformer", "blockType": "DATA_TRANSFORMER", "hasResult": true, "description": "Applies ONE operation from a fixed |
| 11 | get_block_schema | ✅ | true | true | true | true | { "type": "data-transformer", "blockType": "DATA_TRANSFORMER", "hasResult": true, "description": "Applies ONE operation from a fixed |
| 12 | get_block_schema | ✅ | true | true | true | true | { "type": "return-result", "blockType": "COMPOSE_RESULT", "hasResult": false, "description": "Ends the flow — nothing wired after it |
| 13 | add_block | ✅ | true | true | true | true | { "nodeId": "CD3E8443-369F-4D18-BA8C-E84D4BBABEBB", "name": "Parse Numbers", "resultAlias": "Transform Data Result", "type": "data-t |
| 14 | add_block | ✅ | true | true | true | true | { "nodeId": "190A955B-F25D-4390-81D4-B19E774A2560", "name": "Calculate Sum", "resultAlias": "Transform Data Result", "type": "data-t |
| 15 | add_block | ✅ | true | true | true | true | { "nodeId": "F841C5C0-7D73-40AB-BDD0-561485AD0D7F", "name": "Return Sum", "resultAlias": null, "type": "return-result", "issues":  |
| 16 | wire_edge | ✅ | true | true | true | true | { "fromStatus": [], "toStatus": [ "Missing value or expression" ] } |
| 17 | wire_edge | ✅ | true | true | true | true | { "fromStatus": [ "Missing value or expression" ], "toStatus": [] } |
| 18 | configure_block | ✅ | true | true | true | true | { "nodeId": "CD3E8443-369F-4D18-BA8C-E84D4BBABEBB", "name": "Parse Numbers", "resultAlias": "Parsed Numbers", "issues": [] } |
| 19 | configure_block | ✅ | true | true | true | true | { "nodeId": "190A955B-F25D-4390-81D4-B19E774A2560", "name": "Calculate Sum", "resultAlias": "Sum Result", "issues": [] } |
| 20 | configure_block | ✅ | true | true | true | true | { "nodeId": "F841C5C0-7D73-40AB-BDD0-561485AD0D7F", "name": "Return Sum", "resultAlias": null, "issues": [] } |
| 21 | get_flow_summary | ✅ | true | true | true | true | { "nodes": [ { "id": "CD3E8443-369F-4D18-BA8C-E84D4BBABEBB", "type": "DATA_TRANSFORMER", "name": "Parse Numbers",  |
| 22 | get_node_details | ✅ | true | true | true | true | { "id": "F841C5C0-7D73-40AB-BDD0-561485AD0D7F", "type": "return-result", "blockType": "COMPOSE_RESULT", "name": "Return Sum", "res |
| 23 | save_flow | ✅ | true | true | true | true | { "id": "28CC5C2D-9224-4333-AEC9-39A3CB5FE757", "version": 1, "elementCount": 3, "status": "READY", "errorMessage": null } |
| 24 | test_run_block | ✅ | true | true | true | true | { "completed": true, "dataLoadedToS3": false, "elementId": "CD3E8443-369F-4D18-BA8C-E84D4BBABEBB", "elementType": "DATA_TRANSFORMER" |
| 25 | start_flow | ✅ | true | true | true | true | { "ok": true, "result": "" } |
| 26 | stop_flow | ✅ | true | true | true | true | { "ok": true, "result": "" } |

18/18 calls matched the recording. id remaps learned: 7
