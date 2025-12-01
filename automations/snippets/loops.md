In programming and automation, a loop is a way to repeat a set of actions multiple times. Think of it like a washing machine that repeats the same washing cycle until your clothes are clean. Loops help automate repetitive tasks, making processes more efficient and less prone to errors.

## What is a Loop?

A loop allows you to perform a series of steps over and over again until a specific condition is met. Each cycle in a loop is called an **iteration**. This is particularly useful when you need to process a large amount of data, check for updates regularly, or repeat an action until a desired result is achieved. For example, imagine you are managing an email marketing campaign. You want to send a reminder email to all customers who haven't opened your previous email. Instead of manually checking each customer and sending emails one by one, you can use a loop to automate this process:

1. Check the Email Status - look at the status of each customer's email.
2. Send Reminder Email - if the email is not opened, send a reminder.
3. Repeat - continue this process for each customer in your list.

This way, the loop will keep checking and sending emails until it has gone through the entire customer list.

## Loops in FlowRunner

In FlowRunner, loops are implemented using the "Repeat" block. This block allows you to repeat a group of actions, known as a sub-flow, as many times as needed until a specified condition is met. 

![repeat block](../images/repeat-block.png)

## Repeat Block Properties
The "Repeat" block has several unique qualities:

1. **Grouping Blocks**: The Repeat block acts like a container where you can place multiple blocks. These blocks form the sub-flow that will be repeated. For example, you might include blocks to check a condition, perform an action, and then wait for a specified time or a trigger event before checking again. To edit the sub-flow of the Repeat block, click the "expand" icon:
![expand icon repeat block](../images/repeat-block-expand.png)

2. **Condition for Iterations**: The Repeat block includes a condition that determines how many times the loop will run. As long as this condition is true, the Repeat block will keep running the sub-flow. Once the condition is false, the loop stops, and the flow continues to the next block outside the Repeat block.
![repeat condition](../images/repeat-condition.png)
When you click the **Add a Condition** button, you can add a condition the same way as in [other parts where conditions are supported](../flow-editing/conditions.md) of FlowRunner™.
![adding condition in repeat](../images/repeat-condition-added.png)

3. **Current Iteration Number**: FlowRunner™ maintains a special number called the `Current Iteration Number`, which starts at 0 for the first iteration and increments by 1 with each subsequent iteration. This number can be used within your flow to track or control the loop's progress. You can reference `Current Iteration Number` in the "Repeat" condition or in any block in the sub-flow. The `Current Iteration Number` element is available through the [Expression Editor](../flow-editing/expressioneditor.md).
![current iteration number](../images/current-iteration-num.png)

4. **Failsafe Protection Count**: The Repeat block includes a special configuration property called "Failsafe Protection Count". This field allows you to set the maximum number of iterations before the loop stops. This feature is particularly useful during flow development to prevent infinite looping, which can result in an error due to flow execution timeout. It is recommended to set this number to the lowest value that is reasonably high enough for your needs.

    ![failsafe protection count](../images/repeat-fail-safe-protection.png)

Loops in FlowRunner™, facilitated by the Repeat block, enable you to automate repetitive tasks effectively.