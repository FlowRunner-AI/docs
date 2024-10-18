---
icon: material/alpha-e-circle-outline
---
## Overview

FlowRunner is designed to be highly customizable, allowing you to tailor its functionality to suit your specific needs. While FlowRunner offers a range of built-in actions and triggers, you can extend its capabilities by developing **Custom Actions** and **Custom Triggers**. These customizations can either be used internally, within your own apps, or shared with others through the Backendless Marketplace. This flexibility provides both personal extensibility and community-driven enhancements for creating more powerful and personalized workflows.

## Custom Actions

Custom Actions allow you to define new operations that can be used within your flows, just like any of the built-in actions. These are especially useful when your application requires capabilities beyond what’s provided by default. For instance, you may want to:

- **Integrate with third-party APIs or external services**: Custom Actions allow you to connect your app to other systems, enabling tasks like fetching data from external APIs or posting updates to external services.
- **Execute complex business logic**: You might need to handle logic specific to your app, such as calculating custom metrics or performing data transformations that aren’t covered by the default actions.
- **Create reusable operations**: Once you develop a Custom Action, you can use it across multiple workflows, making your workflows more modular and maintainable.

![custom actions](../images/custom-actions.png)

You can build Custom Actions using **Codeless** or **JavaScript (Node.js)** in Backendless. Once developed, these actions can be added to any flow within FlowRunner, offering a seamless way to expand your workflow capabilities.

## Custom Triggers

Custom Triggers allow you to define custom events or conditions that can be used anywhere in your workflows. While triggers are often thought of as starting points, they are not limited to that role. A Custom Trigger can be used at any point within a flow, pausing execution until the trigger is activated. This allows you to:

- **Trigger workflows based on external events**: You can create a Custom Trigger that starts a flow when an external event occurs, such as receiving a webhook from a third-party service.
- **Pause and resume workflows**: Triggers can be placed in the middle of a flow, allowing the flow to pause and wait until the specified trigger condition is met before proceeding.
- **Handle app-specific events**: Custom Triggers can activate flows based on unique app events that are specific to your business logic or data model.

Just like Custom Actions, Custom Triggers can be reused across multiple workflows. Once created, you can integrate them into your flows wherever they're needed, adding flexibility to how and when your workflows operate.

## Backendless Marketplace

The **Backendless Marketplace** serves as a platform where you can share your custom components or find pre-built solutions created by others. This marketplace offers two major benefits: the ability to **share** your own customizations with the Backendless community and the opportunity to **discover** solutions built by others to accelerate your development process.

If you develop Custom Actions or Triggers that could benefit other developers, you can publish them to the Backendless Marketplace. Publishing allows other users to discover, install, and use your actions and triggers in their own flows. Whether you’re sharing freely or offering paid solutions, the marketplace gives you a way to contribute to the community while also potentially monetizing your work.
