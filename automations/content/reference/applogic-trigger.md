The "App Logic Trigger" is a powerful trigger block integrated with the Backendless Codeless system. When a flow instance reaches this trigger, it goes into the waiting mode, nothing in the flow is executed until the trigger is activated. You can customize the trigger by assigning a name to the block that reflects the event that activates the trigger:

![app logic trigger](../images/app-logic-trigger.png)

## Integration with Codeless

When you add an "App Logic Trigger" to a flow, the Codeless toolbar will automatically display a menu item for the flow with the "Run App Logic Trigger" block in it.

![app logic trigger codeless](../images/run-app-logic-trigger-codeless.png)

## Understanding Trigger Activation
Trigger activation is a crucial concept in FlowRunner, and with its various options, it can become quite complex. Understanding all possibilities is essential for efficient flow management.

A general rule to keep in mind is that a flow must be started with the [Call Flow](../flow-execution/overview.md#callflow-commandapi) request. If your flow has a schedule, the FlowRunner scheduler will automatically use the Call Flow request to initiate your flow. Using the Call Flow creates a new instance of your flow, which means you could have multiple instances running simultaneously.

When your flow includes an "App Logic Trigger," some or all instances may reach this trigger and wait for activation. There are three trigger acrivation modes described further in this chapter:
1. The **`Activate All`** option will activate all waiting flow instances, causing all of them to run again. 
2. The **`Activate Any`** option will activate a random flow instance. 
3. Tthe **`Activate Specific`** option will activate a specific instance identified by the provided `executionId` value.

## Activation Modes

The Codeless block for activating the trigger includes an "Activation Mode" option with three supported modes:

![activation modes in codeless](../images/activation-modes-codeless.png)

1. **Activate Any**: If multiple instances of the flow are waiting on the same "App Logic Trigger", this will activate a random flow instance. If the flow starts with an "App Logic Trigger", a new instance will be created.

    !!! note
        If a flow starts with an "App Logic Trigger" and you activate it with the `Activate Any` option, it is the only case when a new instance of a flow is created without a prior `Call Flow` request.

2. **Activate All**: If multiple instances of the flow are waiting on the same "App Logic Trigger", this will activate all of them. If no flows are waiting on the trigger, the request will return an error.
3. **Activate Specific**: Activates a specific flow instance identified by its `executionId`. The `executionId` for this option can be obtained from the result of the [Call Flow](../flow-execution/overview.md#callflow-commandapi) request. For example, the Codeless logic below uses the [Call Flow](../flow-execution/overview.md#callflow-commandapi) request, stores the `executionId` value in `Page Data` and then activates an "App Logic Trigger" with it.

    ![activate flow with executionId](../images/call-flow-and-activate-it.png)

    If a flow instance was started by a scheduler, the flow developer must ensure that the `executionId` value is passed to the application that needs to use it. 



## Passing Data to the Trigger

You can pass data to an "App Logic Trigger" through the "Body" connector on the Codeless block. This connector expects an object and is optional:

![run app logic trigger with body](../images/run-app-logic-trigger-body.png)

Any data passed to the trigger will be available through the Expression Editor as an element with the name assigned to the "App Logic Trigger" block followed by the word "Data":

![app logic trigger data](../images/app-logic-trigger-data.png)

## Additional Configurations

Similar to other trigger blocks, the "App Logic Trigger" can be configured with an activation condition and user authorization constraints. For more information, see the [Required Authentication](./external-callback-trigger.md#required-authentication) and [Conditional Trigger Activation](./external-callback-trigger.md#conditional-trigger-activation) chapters in the [External Callback](./external-callback-trigger.md) section of this guide.