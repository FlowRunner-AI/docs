The **Run API Service** block allows you to call methods from an API service deployed within the same Backendless app where your flow is running. This block provides a simple way to invoke an API service that hasn’t been specifically configured as a custom FlowRunner action. 

If you are already familiar with developing custom FlowRunner actions, this may seem a bit redundant at first. After all, custom actions are implemented as API Services and appear as regular blocks in the Flow Editor. However, there are situations where an API service hasn’t been configured as a FlowRunner block. In those cases, you can still use the **Run API Service** block to invoke the service and execute its operations within your flow.

## Block Configuration

The **Run API Service** block is designed for simplicity. When you add this block to your flow, you’ll be able to choose from a list of available API services that have been deployed in your Backendless app. Once you select a service, the configuration panel will present a list of the service’s available methods or operations.

![run api service demo](../images/run-api-service-demo.png)

Here’s how it works:

1. **Selecting an API Service**: From the configuration panel, you’ll be able to choose the service you want to invoke. All the deployed API services in your Backendless app will be listed.

2. **Selecting a Method**: After selecting the service, the panel will update to show a list of available methods. These methods represent the operations that the API service exposes.

3. **Configuring Method Arguments**: If the method you select requires arguments, the configuration panel will generate a dynamic form for inputting these values. You can bind the method’s arguments to your flow’s data using the **Expression Editor**, making it easy to pass dynamic values from other parts of the flow into the API call.

4. **Handling the Result**: If the API method returns any data, that data will be available as the block’s **result** element in subsequent parts of your flow. You can use this result in later blocks to continue processing or branching the flow based on the API response.

## When to Use the Block

The **Run API Service** block is particularly useful when you want to integrate existing API services into your flows without needing to configure them as FlowRunner custom actions. For example, if you have already deployed API services that handle backend logic - such as user management, data processing, or third-party API integrations - you can easily call these services within your flows using this block.

This block is ideal for situations where:

- **Existing services**: You have deployed services in your Backendless app that aren’t configured as custom FlowRunner actions, but you still need to invoke them.
- **Complex logic**: You need to integrate backend services into your flows to handle complex logic or processes that don’t need to be reimplemented as custom actions.
- **Dynamic input/output**: You want to dynamically pass data from your flow into the service method and handle the service’s result within the flow.

By using the **Run API Service** block, you can quickly extend your flow's functionality and interact with your Backendless API services without any additional setup.

The **Run API Service** block provides a simple and flexible way to integrate API services into your FlowRunner workflows, even if those services aren’t configured as custom FlowRunner actions. By offering access to all the deployed API services in your Backendless app, this block expands the capabilities of your flows and allows you to seamlessly execute service operations within your logic.