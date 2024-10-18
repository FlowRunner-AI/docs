---
icon: material/group
---

Imagine you are orchestrating a complex business workflow with multiple conditions that need to be met before proceeding to the next step. For instance, let's say you are managing an order processing system. You need to ensure that an order confirmation is received, payment is completed, and the inventory is updated before shipping the product. This is where FlowRunner's `Triggers Group` block comes into play.

![triggers group block](../images/triggers-group-block.png)

In FlowRunner, the `Triggers Group` block allows you to pause the flow execution until specific conditions, represented by triggers, are met. This block can contain multiple trigger blocks, each representing a different condition. The triggers within this group are equal; there is no predefined order, and the flow will remain paused until the configured conditions are satisfied.

## Creating a Triggers Group

To configure the Triggers Group block, click the `Expand` icon. This action opens a special editing mode in the Flow Editor that allows you to add other triggers to the group. In this mode, you can add the necessary triggers without needing to connect them in a sequence, as all triggers in a group are equal and do not represent any specific order.

![triggers group expand](../images/triggers-group-expand.png)

## Transition Modes

The Triggers Group block offers flexibility with two Outgoing Transition Modes. You can access the transition mode configuration by clicking the Triggers Group block in your flow to open its properties:

![triggers group transitions](../images/triggers-group-transitions.png)

The first mode, **"When at least one trigger occurs,"** allows the flow to continue as soon as any one of the triggers in the group is activated. This is particularly useful in scenarios where you need to proceed as soon as any condition is met. For example, in our order processing system, you might want to start the shipping process as soon as either the order confirmation or the payment is completed, not necessarily waiting for both.

The second mode, **"When all triggers start within the time set below,"** is designed for more complex scenarios where all conditions must be met within a certain timeframe before proceeding. In the same order processing example, you may want to ensure that both the order confirmation and payment completion happen within, say, 24 hours. If both triggers are activated within this period, the flow will continue to the next step, which might involve updating the inventory and preparing the product for shipment. If not, you might want to take a different action, such as notifying the customer or canceling the order.

## Triggers Group Benefits

Using the `Triggers Group` block, FlowRunner empowers you to design workflows that can adapt to various conditions and requirements. Whether you need to proceed based on the first available trigger or wait for all conditions to be met within a specified timeframe, this feature offers the flexibility to handle both simple and complex scenarios with ease.

In essence, the `Triggers Group` block in FlowRunner is a powerful tool for managing workflow conditions. By allowing multiple triggers to be grouped and providing flexible transition modes, it ensures that your workflows can pause and resume based on precise conditions, making your automation processes more robust and reliable.