---
icon: material/transfer
---

Creating workflows in FlowRunner™ involves dynamic data interactions across various components. Each element within your flow—such as actions, triggers, conditions, utilities, and transformers—handles data in specific ways. These elements take input parameters and produce results that drive your workflow forward. For example, the `Send Email` block requires an email address to send a message, demonstrating how inputs are essential for the block's function.

![Send Email Inputs Demo](../images/send-email-inputs-demo.png)

## Data References

As your flow executes, each block completes its tasks and produces a "result". This result can range from a simple data point to a complex set of information.

!!! note
    Trigger blocks do not produce a "result". Instead, they provide access to the data they have received, which can be used throughout your flows.

For instance, a trigger that activates when a web form is submitted captures the information provided by a customer. This data is stored and can be utilized in subsequent blocks of the flow. You can assign a user-friendly name to each result element, making it easier to reference and manage within the Flow Editor.

![Sample Result](../images/reference-result-as-sample.png)

## Data Transformation

Often, the output from one block needs modification before it can be used by subsequent blocks in the flow. For example, if you need to email a customer who filled out a web form, you might need to extract their email address from the submission data. Transformers and Expressions allow you to adapt incoming data to meet the requirements of downstream tasks.

![Get Email from Result](../images/using-result-to-get-email.png)

[Transformers](../flow-editing/transformer.md) ensure that data passing from one block to another is correctly formatted and structured, facilitating smooth data flow and bridging gaps between different data handling requirements.

Understanding and manipulating data movement within your flows is essential for creating effective automations. It’s not just about connecting blocks; it’s about orchestrating a coherent and efficient flow of information that enhances your business operations. This chapter aims to equip you with the knowledge to navigate and optimize these data interactions, ensuring that each workflow component is purposeful and impactful.