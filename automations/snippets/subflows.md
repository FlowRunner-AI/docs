# SubFlows

SubFlows are reusable workflow sequences that you define once and use multiple times within the same flow. Think of a SubFlow as a packaged set of steps you can place multiple times throughout your workflow.

## Example: Audit Tracking
Consider a workflow that processes financial transactions and must create audit records at multiple steps for compliance. Each audit record requires the same sequence - check configuration settings to determine what to log, format the audit data according to organizational standards, add a timestamp, and save the record to the audit database.
Instead of rebuilding this sequence at each audit point, create a SubFlow called "Create Audit Record" and place it at different points in your transaction workflow:

- After transaction validation (audit the validation result)
- After payment authorization (audit the authorization response)
- After transaction completion (audit the final transaction state)

Each time the SubFlow runs within the transaction workflow, it executes the same audit logic but receives different input values for the event type, transaction ID, and event details.

## Why Use SubFlows

SubFlows help you:

- Avoid duplicating the same workflow logic in multiple places
- Simplify complex flows by breaking them into manageable pieces
- Update logic in one place and have changes apply everywhere the SubFlow is used
- Make workflows easier to read and maintain

## SubFlows vs. Call Flow Action

FlowRunner™ offers two ways to reuse workflow logic:

**SubFlows** are workflow sequences that exist only within the current flow. Use SubFlows when you need to repeat a specific sequence multiple times in the same workflow. SubFlows cannot be called from other flows.

**[Call Flow](../reference/call-flow-action.md) action** invokes a complete, separate flow from within your current flow. Use the Call Flow action when you need to reuse an entire flow across multiple different flows.

## Creating a SubFlow

Locate the **Create SubFlow** button in the Block List panel. This button cannot be dragged to the canvas - click it to open the New SubFlow dialog.

![create subflow button](../images/create-subflow-button.png)

The New SubFlow dialog requests:

**SubFlow Name**  
Enter a descriptive name that indicates what the SubFlow does. This name appears in the Block List panel and helps you identify the SubFlow when building your workflow.

**Input Parameter Names**  
Define the data the SubFlow needs to perform its task. For example, a "Send Order Confirmation" SubFlow might need parameters like `customerEmail`, `orderNumber`, and `orderTotal`. Add additional parameters by clicking the plus icon.

![new subflow popup](../images/new-subflow-popup.png)

Click **CREATE SUBFLOW** to create the SubFlow. The new SubFlow appears in the SUBFLOWS group in the Block List panel.

![subflow created](../images/subflow-created.png)

## Using SubFlows in Your Workflow

Drag the SubFlow from the Block List panel to the Flow Editor canvas. The SubFlow functions like any other action block - connect it to predecessor blocks and add successor blocks after it.

When you select a SubFlow block on the canvas, the settings panel displays input fields for any parameters you defined. Provide values for these parameters using Expression Editor for dynamic values or enter static values directly.

Parameter configuration for SubFlows follows the same rules as other FlowRunner™ blocks. You can reference results from previous blocks, use variables, or apply data transformations through Expression Editor.

![subflow usage](../images/subflow-usage.png)

## Defining SubFlow Logic

When you first create a SubFlow, it contains no logic. You must define what the SubFlow does by adding blocks inside it.

To edit a SubFlow, click the **expand icon** in the lower right corner of the SubFlow block on the canvas. This navigates into the SubFlow editor.

![expand icon subflow](../images/expand-icon-subflow.png)

When editing a SubFlow, the editor title bar displays the SubFlow name, indicating you are working inside that SubFlow. Build the SubFlow's logic the same way you build regular flows - drag blocks from the Block List, configure parameters, and connect blocks to define the execution sequence.

**Important limitation:** SubFlows cannot contain other SubFlows. You can only use standard actions, triggers, conditions, and other flow control blocks inside a SubFlow.

To return to the main flow, click the flow name in the breadcrumb navigation or use the back button in the editor.

## Accessing Input Parameters

Inside a SubFlow, access input parameters through the Expression Editor using the **Input Data** pill. The Input Data pill provides a dropdown list of all declared input parameters for the SubFlow.

To use an input parameter:

1. Open Expression Editor for any parameter field in a block inside the SubFlow
2. Locate the **Input Data** pill in the Expression Editor
3. Click the dropdown on the Input Data pill to see available parameters
4. Drag the Input Data pill into your expression
5. Select the specific parameter from the dropdown

![accessing input subflow](../images/accessing-input-subflow.png)

## SubFlow Reusability

You can place the same SubFlow multiple times in your workflow. Each instance executes the same logic but can receive different input parameters.

For example, your order processing flow might use "Send Order Confirmation" in multiple places:

- After initial order placement (with customer order details)
- After successful payment processing (with payment confirmation details)
- After shipping dispatch (with tracking information)

Each instance receives different input values but executes the same underlying logic.

## Updating SubFlow Logic

When you modify a SubFlow's internal logic, all instances of that SubFlow in your workflow update automatically. If you have three instances of "Send Order Confirmation" and you change how the confirmation email is formatted, all three instances use the updated format immediately.

This ensures consistency across your workflow and eliminates the need to update multiple copies of the same logic.

## SubFlow Results

SubFlows return results that subsequent blocks in your workflow can use. The result structure depends on whether the SubFlow uses Return Result blocks and how many execution branches exist.

### Single Return Result Block

When a SubFlow has only one Return Result block, the result is an object containing the properties and values defined in that Return Result block.

For example, if your Return Result block defines `auditId` and `timestamp`:

![sample return result](../images/subflow-result-sample.png)

 the SubFlow result contains those properties directly:
```json
{
  "auditId": "12345",
  "timestamp": "2025-10-29T10:30:00Z"
}
```

### Multiple Return Result Blocks

When a SubFlow has multiple Return Result blocks (meaning multiple execution branches), the result structure includes the result of the Return Result block that was reached first as well as a list of all Return Result objects. For example, suppose a SubFlow has two Return Result blocks, one shown above and the other shown in the screenshot below:

![multi return result](../images/multi-return-result.png)

The result structure of the sublfow would look as shown below:

```json
{
  "executionId": "BDE51159-E27C-431F-97DC-FEF5D8014481",
  "result": {
    "blockName": "Return Audit Result",
    "data": {
      "auditId": "12345",
      "timestamp": "2025-10-29T10:30:00Z"
    }
  },
  "results": [
    {
      "blockName": "Return Audit Result",
      "data": {
         "auditId": "12345",
          "timestamp": "2025-10-29T10:30:00Z"
      }
    },
    {
      "blockName": "Return Log Status",
      "data": {
        "logCreated": true
      }
    }
  ],
  "status": "COMPLETED"
}
```

The `blockName` value is the actual name assigned to each Return Result block. It is recommended to assign meaningful names to Return Result blocks that represent the result they provide. For example, name blocks "Audit Success" or "Audit Failed" rather than using default names.

### Without Return Result Blocks

If a SubFlow does not use Return Result blocks, the result object will not include any data from the SubFlow.

### Accessing SubFlow Results

Reference SubFlow results in subsequent blocks using Expression Editor.

**For single Return Result:**
```
{{SubFlowBlockName Result->propertyName}}
```

**For multiple Return Results:**

Access the `result` property for the first branch:
```
{{SubFlowBlockName Result->data.propertyName}}
```

Access specific branches from the `results` array:
```
{{SubFlowBlockName Result->[0].data.propertyName}}
{{SubFlowBlockName Result->[1].data.propertyName}}
```

Access execution metadata:
```
{{SubFlowBlockName Result->executionId}}
{{SubFlowBlockName Result->status}}
```

For detailed information about configuring Return Result blocks, see the Return Result documentation.

## When to Use SubFlows

Use SubFlows when:

- You repeat the same sequence of actions multiple times in a workflow
- You want to organize complex workflows into logical sections
- Changes to repeated logic should apply consistently everywhere
- The reusable logic is specific to the current workflow

Use the Call Flow action when:

- You need to reuse complete workflows across multiple different flows
- The logic represents a standalone process
- Multiple teams or projects need access to the same workflow

!!! tip "Best Practices"
    **Naming SubFlows**  
    Use descriptive names that explain what the SubFlow does. Good names include "Validate Customer Data", "Calculate Shipping Cost", or "Send Notification". Avoid generic names like "SubFlow1" or "Process Data".

    **Parameter Design**  
    Define only the parameters the SubFlow actually needs. Too many parameters make SubFlows harder to configure and maintain. If a SubFlow needs many parameters, consider whether it should be broken into smaller SubFlows.

    **Single Responsibility**  
    Each SubFlow should perform one clear task. SubFlows that try to do too many things become difficult to reuse and maintain. If a SubFlow becomes complex, consider splitting it into multiple smaller SubFlows.

    **Documentation**  
    Add comments or notes inside SubFlows to explain complex logic. Future users (including yourself) will appreciate clear explanations of what the SubFlow does and why certain steps are necessary.

    **Testing**  
    Test SubFlows thoroughly before using them in multiple places in your workflow. Bugs in a SubFlow affect every instance where it appears. Use Test Mode to validate SubFlow behavior with different input parameters.