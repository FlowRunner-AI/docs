Conditional logic in FlowRunner allows you to create decision points within your automation, directing the flow based on specific conditions. Think of it as a fork in the road where the flow will follow one path if the condition is met (yes) and a different path if it is not (no). For instance, your flow might take different actions depending on whether it is a weekend or a weekday.

At the heart of every condition is a question that results in a "yes" or "no" answer. Here are some examples:

- Does the order have priority shipping?
- Is this a returning customer?
- Is the current time within business hours?

## Condition Parts

Conditions can be integrated into various parts of your flow, including triggers and the dedicated `Condition` block. Configuring a condition involves building a logical expression that must evaluate to either `true` or `false`. A logical expression consists of one or more "parts." Each "part" performs a single check against a specific value. Here are some examples:

- Is variable `X` greater than 5?
- Does a string in a result element contain the word `"urgent"`?

### Configuring a Part

To configure a "part," you need to specify the following parameters:

1. **Property**: This is the value that will be evaluated. You use the [Expression Editor](./expressioneditor.md) to select this value. It can be any value obtained through the Expression Editor.
2. **Property Type**: This indicates the data type of the value selected in the `Property` field. The options available for the **Operator** parameter depend on the data type. For instance, if the data type is `STRING`, operators like `STARTS WITH`, `CONTAINS`, and `ENDS WITH` will be available. If the data type is `INT`, the operators will include `GREATER THAN`, `LESS THAN`, etc.
3. **Operator**: This is the function to be performed against the value specified in the **Property** parameter. Most operators require an additional value.
4. **Value**: This is the value used by the operator function (if applicable).

Consider the examples below:

1. Check if the `Order Status Result` element's value equals the word `PROCESSED`:

    ![sample condition part string](../images/sample-condition-part-string.png)

2. Check if the `Products Purchased Result` element's value is greater than 10:

    ![sample condition part int](../images/sample-condition-part-int.png)

### Multi-Part Conditions

You can include multiple parts in a logical expression. These parts are "connected" using the `AND` and `OR` operators. Consider the example below. At the bottom of the screenshot, you will see how the parts are connected to create the final logical expression for the condition:

![two parts in a condition](../images/two-parts-in-condition.png)

Clicking the `AND` operator changes it to `OR` and vice versa. FlowRunner uses conventional boolean logic with these operators. Each part is evaluated and results in either `TRUE` or `FALSE`. The following rules apply:

```
TRUE AND TRUE = TRUE
TRUE AND FALSE = FALSE
TRUE OR TRUE = TRUE
TRUE OR FALSE = TRUE
FALSE AND FALSE = FALSE
FALSE OR FALSE = FALSE
```

For expressions with three or more parts, you can assign precedence in the expression evaluation using parentheses. Anything in parentheses is evaluated first. Consider the following example with three parts:

![three parts condition](../images/three-parts-condition.png)

The parts in the condition are organized in the following expression:

![three parts condition zoomed in](../images/three-parts-condition-details.png)

It may be ambiguous how the expression will be evaluated if any part is `FALSE`. To clarify, you can group parts using parentheses.

???+ note
    To add a parenthesis, simply click in the space between the parts and the `AND`/`OR` operators.

Once parentheses are present, it is easier to understand how the expression will be evaluated. The following two examples produce different results depending on how individual parts are evaluated:

![three parts example version 1](../images/three-parts-variation1.png)

or

![three parts example version 2](../images/three-parts-variation2.png)

By organizing your conditions effectively, you can create complex and precise logical flows that ensure your automation behaves exactly as intended.

## Condition Block

The `Condition` block allows you to set up a logical expression and then branches the flow into two paths: `Yes` and `No`. If the expression evaluates to `true`, the flow follows the `Yes` branch. Otherwise, it follows the `No` branch. 

![condition block](../images/condition-block.png)

### Example Flow

Consider a scenario where you want the flow to behave differently based on whether it is a weekend or a weekday. You can set up a condition that checks the current day of the week:

![sample flow with condition](../images/sample-flow-with-condition.png)

The `Condition` block in this example uses the following logic:

![sample condition logic](../images/sample-condition-logic.png)

This logic checks if the `Week Day Number` value is either Saturday (value `6`) or Sunday (value `7`). Based on this check, the flow can take different actions.

- **On Weekends - when `Week Day Number` is greater or equal `6`**: You might want the flow to send an alert to the team informing them of weekend activity, or perhaps delay certain non-urgent processes until Monday.
- **On Weekdays - for all other values stored in `Week Day Number`**: The flow could continue with regular processing, such as sending orders to the shipping department or performing routine updates.

The `Condition` block is highly versatile, enabling you to create complex logical expressions. These expressions can include multiple parts combined using `AND` and `OR` operators. Additionally, the `Condition` block can handle various data types, making it a powerful tool for building sophisticated decision-making processes within your flows. 

For a detailed overview of the `Condition` block's capabilities, refer to the [Condition Block](../reference/condition.md) chapter in the Block Reference section of this guide.

## Conditions with Triggers
All built-in FlowRunner triggers can be enhanced with a condition that acts as a "filter". These conditions follow the same rules described above for configuring logical expressions. When a trigger has an associated condition, it will only be activated if the condition evaluates to `TRUE`. This ensures that your flows only proceed under the specific circumstances you define, adding an extra layer of precision and control to your automation processes.