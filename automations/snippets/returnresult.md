# Return Result

The Return Result block defines the data returned from SubFlows and flows invoked via Call Flow. Use Return Result blocks to structure the output that subsequent workflow steps can access.

## How Return Result Works

Return Result is a terminal block - it marks the end of an execution branch. When a flow reaches a Return Result block, that branch stops executing and the configured data becomes available as the result.

Return Result blocks can be used in:

- **SubFlows** - Define data returned to the parent flow
- **Flows invoked via Call Flow** - Define data returned to the calling flow

The block functions identically in both contexts.

## Configuring Return Result

Configure the return structure in the **Compose Result** section of the block settings.

![return sample](../images/subflow-result-sample.png)

Each row in the Compose Result section consists of:

**Property**  
The name of the property in the returned result object. This field supports Expression Editor, allowing dynamic property names based on workflow data. 

**Value**  
The data to return for this property. This field supports Expression Editor, enabling you to return values from previous blocks, variables, or computed expressions. Values can be static (entered directly) or dynamic (selected through Expression Editor). Click the Expression Editor icon in the field to open Expression Editor.

Add additional properties by clicking the **:material-plus:** icon. Remove properties by clicking the **:material-close:** icon next to the property row.

## Result Structure

The structure of returned data depends on how many Return Result blocks exist in the flow or SubFlow.

### Single Return Result Block

When a flow or SubFlow has only one Return Result block, the result is an object containing the properties and values you configured.

For example, if you configure these properties (see the screenshot above in the [Configuring Return Result](#configuring-return-result) section):

- `auditId` with value `"12345"`
- `timestamp` with value `"2025-10-29T10:30:00Z"`

The result structure is:

```json
{
  "auditId": "12345",
  "timestamp": "2025-10-29T10:30:00Z"
}
```

### Multiple Return Result Blocks

When a flow or SubFlow has multiple execution branches with Return Result blocks, the result structure includes both the first-reached result and a complete list of all results:

```json
{
  "executionId": "BDE51159-E27C-431F-97DC-FEF5D8014481",
  "result": {
    "blockName": "Audit Success",
    "data": {
      "auditId": "12345",
      "status": "completed"
    }
  },
  "results": [
    {
      "blockName": "Audit Success",
      "data": {
        "auditId": "12345",
        "status": "completed"
      }
    },
    {
      "blockName": "Audit Failed",
      "data": {
        "errorCode": "E401",
        "errorMessage": "Validation failed"
      }
    }
  ],
  "status": "COMPLETED"
}
```

The `result` property contains the data from the Return Result block that was reached first. The `results` array contains data from all Return Result blocks across all branches. The flow waits until all branches complete before returning results.

## Naming Return Result Blocks

The `blockName` value in the result structure comes from the name you assign to the Return Result block. Use the **Name** field in the block settings to provide meaningful names.

Good naming practices:

- Use names that describe what the result represents: "Success Response", "Error Details", "Validation Result"
- Avoid generic names like "Return Result" or "Return Result (2)"
- Use names that help identify which branch produced the result: "Payment Approved", "Payment Declined"

Meaningful names make it easier to identify and access specific results when working with multiple Return Result blocks.

## Using Expression Editor

Both the Property and Value fields support Expression Editor. You can use dynamic property names and compute values using any valid Expression Editor syntax, including data from previous blocks, variables, transformations, and conditional logic.

## Data Types

Return Result blocks support all FlowRunner™ data types. The data type is preserved when returned to the calling context.

## Accessing Returned Data

Access returned data in subsequent blocks using Expression Editor. The return structure is the same whether Return Result is used in a SubFlow or a flow invoked via Call Flow - only the block name differs.

**For single Return Result:**

```
{{SubFlowBlockName Result->propertyName}}
```

**For multiple Return Results:**

Access the first-reached result:

```
{{BlockName Result->data.propertyName}}
```

Access specific branches from the results array:

```
{{BlockName Result->[0].data.propertyName}}
{{BlockName Result->[1].data.propertyName}}
```

Access execution metadata:

```
{{BlockName Result->executionId}}
{{lockName Result->status}}
```

```
{{BlockName Result->propertyName}}
```

Replace `BlockName` with either the SubFlow block name or the Call Flow block name depending on which invoked the flow containing the Return Result block.

!!! tip "Best Practices"

    **Use Meaningful Property Names**  
    Choose property names that clearly describe the data they contain. Use `customerEmail` instead of `email`, or `orderTotal` instead of `total` when the context matters.

    **Return Only Necessary Data**  
    Include only the data that calling flows or blocks actually need. Returning excessive data makes results harder to work with and can impact performance.

    **Consistent Structure Across Branches**  
    When using multiple Return Result blocks, maintain consistent property names across branches where possible. This makes it easier to process results regardless of which branch executed.

    **Document Complex Results**  
    Add comments in your flow to document the structure of returned data, especially when returning complex objects or arrays. Future users will appreciate understanding what each property represents.

    **Test Return Result Configuration**  
    Use Test Mode to verify that Return Result blocks return the expected data structure and values. Check both single-path and multi-branch scenarios.