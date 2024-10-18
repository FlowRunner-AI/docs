---
icon: material/emoticon-cool-outline
---

Custom actions in FlowRunner allow you to extend the functionality of your flows by embedding custom logic that you’ve implemented. Whether you need to process data, interact with external APIs, or automate specific tasks, custom actions give you the flexibility to build and integrate any type of functionality into your flow.

Custom actions can be implemented using either **Codeless** (drag-and-drop logic) or **Node.js**, depending on your preference and requirements. Once deployed, these actions become part of the FlowRunner environment and can be used just like any other block in the Flow Editor. For an indepth look see the [Custom Actions](../extensibility/custom-action.md) section of this guide.

## Implementing Custom Actions

You have the freedom to create custom actions that handle various types of logic. These actions can interact with external services, manipulate data, or perform complex logic, and they are particularly useful when you need to execute tasks that go beyond the built-in FlowRunner blocks. Custom Action development workflow is described in detail in the [Action Development](../extensibility/action-development.md) section of this guide.

If your custom action interacts with an external service provider that requires OAuth2 authorization, you can easily integrate [OAuth2 into the action](../extensibility/oauth2-services.md). This ensures that your action can securely access third-party services, such as APIs, using proper authentication. FlowRunner handles the OAuth2 workflow for you, making it easy to implement authorization in custom actions.

## Using Custom Actions

Once you deploy a custom action through **Cloud Logic**, it automatically appears in the **Blocks Toolbox** of the Flow Editor. From there, you can drag and drop it into your flow and connect it to other blocks just like any built-in block. 

![custom actions in flow editor](../images/custom-actions-toolbox.png)

Custom actions fully integrate into the FlowRunner environment, allowing you to:

- Use them in flows by linking them with other blocks.
- Test and debug them directly in the Flow Editor using [Test Mode](./testing.md).

This seamless integration ensures your custom actions work smoothly alongside all other blocks in FlowRunner.

## Installing from the Marketplace

In addition to creating your own custom actions, FlowRunner allows you to install pre-built custom actions from the **Backendless Marketplace**. These marketplace actions can be added to your flows and used immediately, saving you time and effort. Whether you’re looking for specific functionality or want to explore available integrations, the marketplace offers a wide variety of ready-to-use actions that you can install and customize.

Custom actions in FlowRunner empower you to extend your flows with powerful, reusable logic. Whether you implement them using Codeless or Node.js, these actions integrate smoothly with the Flow Editor, providing flexibility and functionality. With the added benefit of OAuth2 support and the ability to install actions from the marketplace, you have everything you need to build and enhance your flows with ease.