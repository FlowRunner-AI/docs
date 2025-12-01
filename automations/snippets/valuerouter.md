The Value Router block is a versatile routing utility in FlowRunner that allows you to dynamically direct flow execution based on evaluated values. By defining multiple branches with flexible matching criteria, it enables you to split workflows into precise execution paths based on data content, user inputs, or computed results. The block provides sophisticated routing logic while maintaining clean, readable workflow designs.

The Value Router block evaluates a single input value against multiple branch conditions and routes execution to the appropriate path. Whether you need simple equality matching, collection-based routing, or range-based decisions, this block provides the flexibility to handle complex routing scenarios with precision and clarity.

Common use cases include routing based on user roles or permissions, directing workflows based on data categories or types, implementing approval workflows with different paths for various scenarios, handling API responses with multiple possible outcomes, and creating dynamic workflows that adapt to changing business rules or thresholds.

![value router example](../images/value-router-example.png)

## Block Configuration

The Value Router block consists of a primary evaluation field and multiple branch configurations that define the routing logic.

### Value to Evaluate

The "Value to Evaluate" field specifies the data that will be compared against branch conditions to determine routing. This field supports the Expression Editor, allowing you to select values from previous blocks, trigger data, or computed expressions.

![value router setup](../images/value-router-setup.png)

!!! example "Common Evaluation Sources"

    - User attributes: `User.role`, `User.department`, `User.accountType`
    - API response data: `APIResponse.status`, `APIResponse.category`
    - Computed values: `OrderTotal.amount`, `ProcessingResult.score`
    - Trigger data: `WebhookData.eventType`, `FormSubmission.priority`

The value you specify here becomes the basis for all branch matching logic, so choose data that provides meaningful differentiation for your workflow routing needs.

## Branch Configuration

The Value Router block allows you to create multiple branches, each representing a different execution path based on specific matching criteria. You can add as many branches as needed to handle your routing scenarios, with each branch configured independently.

**Available Branch Types**:

- **Single Value Matching**: Route when the evaluated value exactly equals one specific value
- **Collection Matching**: Route when the evaluated value matches any value from a specified list
- **Range Matching**: Route when the evaluated value falls within a numeric range

Each branch operates independently, and the Value Router will route to the first branch whose conditions are met, making branch order important for overlapping conditions.

![value router branch setup](../images/value-router-branch-setup.png)

Each branch in the Value Router represents a potential execution path with its own matching criteria. You can create multiple branches to handle different scenarios and values.

### Branch Name

The Branch Name field assigns a descriptive label to each routing path. This name becomes the connector label on the block, making your workflow more readable and self-documenting.

!!! tip "Naming Best Practices"

    - Use descriptive names that clearly indicate the routing purpose
    - Examples: "Admin Users", "High Priority Orders", "Approved Status", "Weekend Processing"
    - Avoid generic names like "Branch 1" or "Option A"
    - Consider using business terminology that stakeholders will understand

### Value Mode Options

The Value Mode dropdown determines how the branch matching logic operates, providing three distinct matching patterns for different use cases.

#### Single Value

When "Single Value" is selected, the branch matches when the "Value to Evaluate" exactly equals the specified value. This mode is ideal for precise matching scenarios.

**Single Value Configuration**:

- **Value Field**: Input field supporting Expression Editor for dynamic values
- **Matching Logic**: Exact equality comparison
- **Use Cases**: User roles, status codes, specific categories, boolean flags

!!! abstract "Example Configuration"

      | Field | Value |
      |-------|-------|
      | **Branch Name** | Admin Access |
      | **Value Mode** | Single Value |
      | **Value** | "administrator" |

      This branch activates when `Value to Evaluate` equals exactly "administrator".

---

#### Collection of Values

The "Collection of Values" mode allows you to specify multiple values that can trigger the same branch. If the "Value to Evaluate" matches any value in the collection, the branch is selected.

**Collection Configuration**:

- **Multiple Value Fields**: Add values using the "+" button
- **Expression Editor Support**: Each field supports dynamic values
- **Matching Logic**: OR logic - matches if evaluation equals any specified value
- **Use Cases**: Multiple user roles, various status categories, different product types

!!! abstract "Example Configuration"

      | Field | Value |
      |-------|-------|
      | **Branch Name** | Management Access |
      | **Value Mode** | Collection of Values |
      | **Value 1** | "manager" |
      | **Value 2** | "supervisor" |
      | **Value 3** | "director" |

      This branch activates when `Value to Evaluate` equals "manager", "supervisor", or "director".

---

#### Range of Values

The "Range of Values" mode enables numeric range matching, routing execution when the evaluated value falls within specified boundaries.

**Range Configuration**:

- **From Field**: Lower boundary (inclusive)
- **To Field**: Upper boundary (inclusive)
- **Expression Editor Support**: Both fields support dynamic values
- **Matching Logic**: Inclusive range check (From ≤ value ≤ To)
- **Use Cases**: Order amounts, user ages, scores, quantities, time periods

!!! abstract "Example Configuration"

      | Field | Value |
      |-------|-------|
      | **Branch Name** | High Value Orders |
      | **Value Mode** | Range of Values |
      | **From** | 1000 |
      | **To** | 5000 |

      This branch activates when `Value to Evaluate` is between 1000 and 5000 (inclusive).

## Default Routing with Everything Else

The Value Router automatically includes an "Everything Else" branch that handles cases where the evaluated value doesn't match any configured branch criteria. This ensures robust workflow execution even with unexpected data.

!!! info "Everything Else Branch Features"

    - **Automatic Inclusion**: Always present, no configuration required
    - **Fallback Logic**: Activates when no other branches match
    - **Error Prevention**: Prevents workflow failures from unmatched values
    - **Debugging Aid**: Useful for logging unexpected values or implementing fallback actions

??? example "Common Everything Else Uses"

    - Error logging and notification
    - Default processing paths
    - Fallback business logic
    - Data validation and quality checks

## Execution Flow and Branch Selection

The Value Router evaluates branches in the order they are configured and routes to the first matching branch. Understanding this evaluation order helps you design effective routing logic.

### Evaluation Process

1. **Value Assessment**: The "Value to Evaluate" is computed using current workflow context
2. **Branch Testing**: Each branch is tested in configuration order
3. **First Match Selection**: The first branch meeting its criteria is selected for execution
4. **Everything Else Fallback**: If no branches match, the Everything Else path is taken

### Branch Priority Considerations

Since evaluation stops at the first match, arrange branches strategically:

- Place more specific conditions before general ones
- Order range conditions to avoid overlap conflicts
- Consider the likelihood of different values when ordering branches
