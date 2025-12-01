# Call Flow Block

The Call Flow block enables your workflow to execute other flows within your FlowRunner™ workspace, creating modular and reusable automation patterns. This block acts as a bridge between flows, allowing you to break complex processes into smaller, manageable components that can be called from multiple workflows.

This capability is essential for building scalable automation architectures where common functionality can be centralized and reused across different workflows. Whether you need to perform standard data validation, execute shared business logic, or trigger related processes, the Call Flow block provides the flexibility to compose sophisticated workflows from reusable building blocks.

Common use cases include calling data processing flows from multiple entry points, executing validation routines across different workflows, triggering notification flows from various business processes, implementing shared calculation logic, and creating modular approval workflows that can be invoked from different contexts.

## Input Configuration

The Call Flow block offers comprehensive configuration options to control how flows are called, what data is passed between them, and how execution is managed.

![call flow config](../images/call-flow-config.png)

### Flow Selection

The Flow dropdown lists all available flows in your current workspace. 

!!! info "Called Flow Requirement"
    Only flows that have been started and are in the `LIVE` state can be called from other workflows.

The dropdown includes a refresh icon that allows you to update the list of available flows without leaving the current workflow editor. This is particularly useful when collaborating with team members or when you've created new flows in separate browser windows.

**Flow Selection Guidelines**:

- All flows appear in the dropdown, but only flows in `LIVE` state can be executed/called using the Call Flow block 
- All flows within your workspace/account are available for selection
- Use the refresh icon to update the list after creating new flows
- Choose flows that are designed to be called by other workflows for best results

### Initial Parameters

The Initial Params section allows you to pass data from the current workflow to the called flow. This composite element consists of Property and Value field pairs that can be added using the "+" button.

**Property Field**: A simple text input where you specify the parameter name. This name will be used to access the data in the called flow through the Expression Editor's "Initial Data" element.

**Value Field**: Supports the Expression Editor, allowing you to pass dynamic data from previous blocks in your current workflow. You can pass any data type including strings, numbers, objects, and arrays.

**Parameter Configuration Examples**:

- Property: `userId`, Value: `${UserRegistration.id}`
- Property: `orderData`, Value: `${OrderProcessing.orderDetails}`
- Property: `validationRules`, Value: `{"minAge": 18, "requiredFields": ["email", "name"]}`

The parameters you define here become available in the called flow through the Expression Editor as `Initial Data.userId`, `Initial Data.orderData`, etc.

### Execution Control

The "Wait for Execution" toggle determines whether the current flow waits for the called flow to complete before proceeding to the next block.

**Synchronous Execution (Toggle Enabled)**:

- Current flow pauses until called flow completes
- If the called flow uses a "Return Result" block, that returned value becomes the result of the Call Flow block
- Best for scenarios where you need the called flow's output before proceeding
- Useful for validation flows, calculation flows, or data transformation flows

**Asynchronous Execution (Toggle Disabled)**:

- Current flow continues immediately after initiating the call
- Call Flow block returns an `executionId` for the started flow
- Best for triggering independent processes like notifications, logging, or parallel workflows
- Useful for fire-and-forget scenarios where the calling flow doesn't need to wait

### User Session Management

The User Session Source dropdown controls how user identity and authentication information is passed to the called flow.

**Available Options**:

**None**: No user information is passed to the called flow. The called flow executes without any user context.

**Execution Init User**: Passes the user object that was provided when the current flow started. This maintains the original user context throughout the flow chain.

**Trigger User**: Passes the user object from a specific trigger within the current flow. When this option is selected, a second dropdown appears allowing you to choose which trigger's user information to pass.

The trigger selection dropdown shows all preceding triggers in the current flow that have captured user information, such as External Callback triggers that received user-token headers.

## Understanding the Results

The Call Flow block's result depends on the execution mode and whether the called flow returns data.

### Synchronous Execution Results

When "Wait for Execution" is enabled, the block result depends on the called flow's behavior:

**With Return Result Block**:
If the called flow includes a "Return Result" block, the data returned by that block becomes the Call Flow block's result.

```json
{
  "validationStatus": "passed",
  "processedData": {
    "userId": 12345,
    "score": 85.5
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Without Return Result Block**:
If the called flow doesn't explicitly return data, the Call Flow block returns an object with the `executionId` property and its value.

### Asynchronous Execution Results

When "Wait for Execution" is disabled, the Call Flow block immediately returns an execution identifier:

```json
{
  "executionId": "550e8400-e29b-41d4-a716-446655440000"
}
```

This execution ID can be used to track or query the status of the called flow through other mechanisms if needed.

### Accessing Results

The Call Flow results become available to subsequent workflow blocks through the Expression Editor, just like any other block result.

**Common Access Patterns**:

- `CallFlowResult.validationStatus`: Accessing returned data from synchronous calls
- `CallFlowResult.executionId`: Accessing execution ID from asynchronous calls
- `CallFlowResult.processedData.userId`: Accessing nested data structures

## Configuring the Block

Like all FlowRunner™ blocks, you can customize how the Call Flow block appears in your workflow and how its results are referenced by subsequent blocks.

### Block Naming

Use the "Name" field to assign a descriptive name that reflects the block's purpose in your workflow. Examples include "Validate User Data," "Process Order Items," or "Send Notification" to make your workflow more readable and maintainable.

### Result Reference

The "Reference Result Data As" field determines how other blocks in your workflow access the Call Flow results. Choose clear, descriptive names like "ValidationResult" or "ProcessingOutput" that make sense when building expressions in subsequent blocks.

## Implementation Strategies

### Modular Workflow Design

Design called flows to be self-contained and reusable. Create flows that perform specific functions and can be called from multiple contexts. This approach promotes maintainability and reduces duplication across your automation system.

### Parameter Standardization

Establish consistent parameter naming conventions across your workspace. Use clear, descriptive property names that make it easy to understand what data is being passed between flows.

### Error Handling Patterns

For synchronous calls, implement error handling in both the calling and called flows. The called flow should use Return Result blocks to communicate success or failure status, while the calling flow should check results and handle different scenarios appropriately.

### User Context Management

Carefully consider which user context to pass to called flows. Use "Execution Init User" for maintaining original user identity throughout a process chain, or "Trigger User" when you need to pass specific user information from particular trigger events.

### Performance Considerations

Use asynchronous calls for operations that don't require immediate results, such as logging, notifications, or background processing. Reserve synchronous calls for scenarios where you genuinely need the called flow's output before proceeding.

### Flow State Management

Ensure called flows are in LIVE state before deploying workflows that depend on them. Implement testing procedures to verify that all flow dependencies are properly deployed and functional.

### Debugging and Monitoring

When using Call Flow blocks, consider how to track execution across multiple flows. For asynchronous calls, the execution ID can be valuable for monitoring and debugging purposes. For synchronous calls, ensure that error conditions in called flows are properly communicated back to the calling flow.