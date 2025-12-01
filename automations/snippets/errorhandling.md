Errors are a natural part of workflow automation. Anticipating and managing them effectively ensures your automations remain reliable and resilient. FlowRunner™ offers error-handling tools to help your workflows recover gracefully from issues like failed service calls, database errors, or invalid input data.  

## Common Error Scenarios  

Errors in your workflows can arise from various sources, including:  

- **External Services**: Failures in API requests due to service downtime or error responses.  
- **Database Queries**: Issues like malformed queries or insufficient permissions.  
- **Invalid Inputs**: Actions failing because of incorrect or missing data.  
- **File Uploads**: Problems caused by network interruptions or file size limits.  

## The Handle Error Block

The **Handle Error** block is a specialized mechanism for managing errors in your flows. Unlike action or trigger blocks, it acts as a fallback route for your flow when errors occur.  

### How It Works  
When you connect a block to the **Handle Error** block, any errors in that block redirect the flow to the **Handle Error** block. From there, successors define how the error is handled. For example, you could log the error, notify an admin, or call another flow to recover from the issue.

In the example below, if the **Retrieve Orders** block encounters an error, control passes to the **Handle Error** block, which directs it to the **Log Error** block. If no error occurs, the flow continues to **Process Orders**:  
![error handler sample flow](../images/error-handler-sample-flow.png)  

## Error Types  

Errors in FlowRunner™ fall into two categories:  

- **Handled Errors**: These are errors connected to a **Handle Error** block. The flow knows how to respond and continues executing.
- **Unhandled Errors**: These occur when no **Handle Error** block is connected. They cause the flow to stop unexpectedly.  

## Error Structure  

Errors are represented as a key/value structure with three main properties:  

- **`code`**: A numeric identifier for the specific error type.  
- **`message`**: A text description of the error, useful for troubleshooting.  
- **`source`**: The name of the block where the error occurred, especially helpful when reusing a `Handle Error` block.  

## Accessing Error Information  

When an error is handled, successors of the **Handle Error** block can access error details via the `Handle Error Result` in the [Expression Editor](../flow-editing/expressioneditor.md). This information allows you to implement custom error-handling strategies based on the error’s properties:  

- Use the `code` to classify the error type.  
- Log meaningful details from the `message`.  
- Trace the origin of the error using the `source`.  

### Conditional Error Handling Example  

Conditional logic can be used to respond differently based on the `code` or other error properties. For instance, you might:  

- Retry a failed action if the error code indicates a temporary issue.  
- Log and notify administrators for critical errors.  
- Redirect to a fallback process for non-recoverable errors.  

The example below shows how to use a condition block to handle specific errors based on their `code`:  
![condition error checking](../images/condition-error-checking.png)  

This approach enables tailored responses to errors, ensuring your workflows remain resilient and adaptable.  

## Best Practices for Error Handling  

1. **Identify Error-Prone Blocks**: Recognize which blocks may encounter errors, such as external service calls or database queries.  
2. **Use `Handle Error` Blocks**: Connect these blocks to `Handle Error` blocks to ensure proper handling. You can centralize error handling or use multiple `Handle Error` blocks for different errors.  
3. **Define Recovery Strategies**: Plan how to respond to errors, such as:  

   - Logging the error for analysis.  
   - Sending notifications to administrators.  
   - Retrying the action after a delay (use the [Wait Block](../flow-editing/waitblock.md)).  
   - Switching to fallback options, like an alternative service.  
   - Calling another flow for advanced error handling (see [Call Flow Action](../reference/call-flow-action.md)).  

By following these best practices, you can create workflows that are resilient to unexpected issues and maintain operational stability.  