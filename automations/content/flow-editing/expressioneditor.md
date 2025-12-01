---
icon: material/exponent
---

In your flow, individual blocks generate data that can be utilized throughout the workflow. Triggers receive and pass on information, actions and transformers create new data, and data buckets store various data elements under logical names. As discussed in the [Data Movement in Flows](dataflow.md) section, a block's inputs can reference the results from other blocks, enabling dynamic and interconnected workflows. This result-to-input data referencing is made possible through the Expression Editor.

## Accessing the Expression Editor
You can open the Expression Editor from any block's input parameter that displays the specific icon:

![accessing expression editor](../images/expression-editor-field.png)

## Accessing Flow Data
When you launch the Expression Editor, it presents a list of all data elements available to the block in the flow. **The system composes the list based on the block's predecessors**. Consider the screenshot of Expression Editor below:

![sample expression editor](../images/sample-expression-editor.png)

The screenshot shows the following sections and elements:

* **Block Results** - `Customer Data`, `Order`, `Initial Form` - these are "result" blocks from the predecessor actions and triggers.
* **Error Handler Results** - `Handle Error Result` - contains a reference to an error channelled through the **[Error Handler](./error-handling.md)** block.
* **User References** - `Initial Form - User` - a reference to a Backendless user (if one is present) when the `Initial Form` trigger was activated.
* **Data Transformation Results** - `Customer Name` - a reference to a result from a Transformer predecessor block.
* **Variables** - `My Vars - New Order ID` - a reference to the `New Order ID` variable in the `My Vars` data bucket. 

## Composing an Expression
To create an expression, you need to arrange one or more elements in the **EXPRESSION** field. There are several rules for working with the elements in the **EXPRESSION** field:

* To add an element to the field, either drag or double-click it. 
* Elements added to the expression can be rearranged by dragging them into the new position.
* To remove an element from the field either drag it outside of the field or click to select it and then use the ++backspace++ keyboard button.
* Use the parenthesis operators ![right parenthesis](../images/right-paren.png){ .skip-lightbox .midalign } and ![left parenthesis](../images/left-paren.png){ .skip-lightbox .midalign} to change the precedence of other operators in the expression evaluation. 
* To copy your expression (so you can paste it elsewhere) use the :fontawesome-solid-copy: icon located to the right of the EXPRESSION field.
* To remove all elements and clear out an expression, click the :fontawesome-regular-trash-can: icon located to the right of the EXPRESSION field.

## Working with Key/Value Structures
For the key/value structures, the Expression Editor implements a special "shortcut" for accessing values by key name. To access value for a key, double-click or drag an element into the **EXPRESSION** field. Click it and you will see an input field for the key/property name. Type in a key name and press `Enter`. The element is reconfigured to access value by key name.
<div style="position: relative; padding-bottom: calc(53.26821938392187% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/VSAq33g0H41UQ8oi3rGA?embed&show_copy_link=true" title="Accessing values in key/value data structures" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>

## Scalar/Constant Data
In addition to referencing flow data (actions/triggers/transformers results and variables), your expressions can include scalar numeric and text (string) data. This is possible with the `Text Input` and `Number Input` elements. These elements can be combined with other scalar or dynamic elements to create more complex expressions.

## Operators
The Expression Editor is not just a gateway to access accumulated data but also a powerful tool for manipulating it. It supports basic arithmetic operations, logical comparisons, and string concatenation, allowing you to construct expressions that yield boolean, numeric, or string results. You can find all supported logical and arithmetic operators in the `OPERATORS` section.

Here are some examples of what you can achieve with the Expression Editor:

- **Arithmetic Operations**: You can perform calculations such as adding, subtracting, multiplying, or dividing numbers. For instance, if you have two numeric data elements representing quantities, you can create an expression to find their sum.

- **Logical Comparisons**: The Expression Editor enables you to create conditions using logical operators like `AND`, `OR`, `EQUALS`, `NOT EQUALS` and `GREATER`/`LESS THEN`. For example, you can compare two values and produce a boolean result that triggers subsequent actions based on the comparison.

- **String Concatenation**: Combine multiple string elements into a single string. This is useful for constructing messages, URLs, or any other text-based data that needs to include dynamic elements from your flow. String concatenation can be implicit by positioning two string elements adjacent to each other, or explicit by using the `+` operator.

## Common Values  

The **Common Values** section provides a set of built-in values that can be used to simplify the creation of expressions. These values are particularly useful for inserting common constants, placeholders, or system-generated data.  

- **Null**: Represents a null value, typically used to indicate the absence of a value or an undefined state.  
- **Yes**: A Boolean value representing `true`.  
- **No**: A Boolean value representing `false`.  
- **Tab**: Inserts a tab character (`\t`), commonly used for formatting text or data.  
- **Space**: Represents a single space character, useful for text concatenation or formatting.  
- **New Line**: Inserts a newline character (`\n`), used to move text to the next line.  
- **Empty Text**: Represents an empty string (`""`), often used as a placeholder or to reset text values.  
- **Empty List**: A placeholder for an empty collection, useful for initializing lists without predefining elements.  
- **Empty Object**: Represents an empty object, often used for initializing object structures.  
- **Carriage Return**: Inserts a carriage return character (`\r`), used in text formatting and some legacy systems.  
- **Current Time**: Returns the current system time, useful for timestamping or time-based logic in workflows.  
- **Math PI**: Represents the mathematical constant π (approximately 3.14159), commonly used in calculations involving circles or angles.  
- **Random Number**: Generates a random number, useful for scenarios requiring randomization or uniqueness.  
- **UUID**: Produces a universally unique identifier, ideal for generating unique keys or identifiers for records and processes.  

## Flow Context
In FlowRunner™, every running flow instance is accompanied by a **Flow Context** - a specialized data collection that stores all information generated during the flow’s execution. This concept is central to how FlowRunner™ manages and organizes data for each flow instance, ensuring seamless automation and precise data tracking.  

The Flow Context is a dynamic collection of data maintained by FlowRunner™ for every running flow instance. It acts as a central repository where:  

- **Block results** are stored after each block’s execution.  
- **Variables** defined within the flow are tracked.  
- **Data transformation values** processed during the flow are preserved.  

Flow builders (developers) do not interact with the Flow Context directly. Instead, the **Expression Editor** provides a user-friendly interface to access all the data stored in the Flow Context.  

In addition to block-specific results and variables, every Flow Context includes several special values that provide critical information about the flow instance. These values can be accessed exclusively through the **Expression Editor**:  

![flow context values in expression editor](../images/flow-context-values.png)

* **Execution ID**  
A unique identifier for the specific instance of the running flow. Use this ID for tracking or logging purposes, especially when troubleshooting or analyzing flow executions.  

* **Flow ID**  
A unique identifier for the flow itself. This value helps differentiate between multiple flows running in the same environment.  

* **Initial Data**  
A key/value structure containing any data sent to the flow when it was triggered using the [**CallFlow API**](../flow-execution/overview.md#callflow-commandapi). If no data was passed or if the flow was started on a schedule, this value will be empty.  

* **Application ID**  
The unique identifier of the Backendless application where the flow is running. This is particularly useful for multi-tenant environments or when integrating with external systems.  

* **Initial User**  
A key/value structure containing the properties and values of the user whose identity was used to create the flow instance. This value is available only for flows triggered via the [**CallFlow API**](../flow-execution/overview.md#callflow-commandapi) and is empty for scheduled flows or flows triggered anonymously.  

By mastering the Expression Editor, you can enhance the functionality of your flows, ensuring that the data moves seamlessly and transforms as needed to meet your automation requirements. This chapter aims to provide you with the knowledge to effectively use the Expression Editor, empowering you to create more sophisticated and responsive workflows.