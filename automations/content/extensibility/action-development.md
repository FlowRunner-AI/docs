---
icon: material/plus-network-outline
---
# Lifecycle of Action Development

Developing a FlowRunner action follows a structured lifecycle, which involves creating the API service, defining operations, adding the logic, and configuring the operation for FlowRunner. Below is an overview of each stage in the lifecycle:

## 1. Create the API Service
The first step in developing a custom action is to create an API service within Backendless. This service acts as a container for one or more operations. Each operation can later be transformed into an action that is usable in FlowRunner. To create a new API service, navigate to the `API Services` screen and click the :material-plus: icon:

![api services create new service](../images/api-services-create-new-service.png)

A popup window opens and defaults to `CODELESS`. Assign a name for your service in the **Service Name:** field and click `SAVE`.

!!! note
    If you plan to develop an action for a service that requires OAuth2 authentication, make sure to select the **With OAuth2 Authorization** template. There are several additional requirements for implementing an action for an service with OAuth2 authorization. Make sure to read the details in the [OAuth2 Authorization](./oauth2-services.md) chapter of this guide. 

## 2. Define Operations
Once the API service is created, you can define specific **operations** within it. These operations represent the individual tasks or logic that will be turned into actions. An API service can have multiple operations, each serving a different purpose, such as interacting with a database, processing user input, or connecting to external services. When you create a new service, the system will automatically prompt you to create an operation by displaying the popup shown below, this is where you will be declaring an operation in your service. An operation must have a name and a description. Depending on what the operation does, you may also need to declare operation parameters.

![new codeless operation](../images/new-codeless-operation.png)

If you need to add an operation (also known as "method"), click the  :material-plus: icon for your service as shown below:

![new method](../images/add-method-service.png)

## 3. Mark an Operation as a FlowRunner Action
To make an operation available and usable in FlowRunner, it must be marked as a **FlowRunner Action**. This step ensures the operation appears as a draggable block in the FlowRunner toolbox, allowing it to be used in flows. To mark your operation as a FlowRunner Action, click the **Register as a FlowRunner Action** togle:

![register as flowrunner action](../images/register-as-flowrunner-action.png)

When marking an operation as a FlowRunner Action, developers can:

- **Set an Icon**: Assign an icon that represents the action, making it easier to identify in the FlowRunner Flow Editor. The icon will appear in a block representing the action in Flow Editor.
   
    ![set action icon](../images/set-action-icon.png)

- **Customize the Block’s Appearance**: Apply a custom color to the block’s border to help distinguish it from other actions. The border can consist of two colors which, if they are different, will gradient from one to the other. By default, the colors are "linked", which means if you change onethe one on the left, the other will automatically change to the same color. However, you can click the :link: icon to unlink the colors, or simply pick another color with the color picker on the right which will remove the linking:

    ![action border colors](../images/action-border-colors.png)

- **Provide a Description**: Add a detailed description that will appear as a tooltip when users hover over the action block, explaining what the action does.

    ![action description](../images/action-description.png)

    The action's block in a flow (and in the FlowEditor toolbox) will show the description:
    ![block with description](../images/action-with-tooltip.png) 

## 4. Define Service Configuration Parameters
In some cases, the operations of your service (i.e., FlowRunner Actions) may require configuration information provided in advance. For example, consider a service designed to send and receive emails. To connect to an email server, the service needs details such as the server’s address, port, username, and password. This information can be collected through **service configuration parameters**.

Configuration parameters can be set up in the **Service Configuration** popup. To access this popup, select your service on the **API Services** screen and click the settings icon:

![configure active service](../images/configure-active-service.png)

These parameters ensure that necessary configuration data is available for your operations without requiring it to be hard-coded or manually entered each time the action is used. For more information on setting up configuration parameters, see the [Service Config Parameters](./service-config.md) section of this guide.


## 5. Develop Action Logic
This is the stage where the actual **logic** of the action is implemented. Depending on your development approach, this step can be handled in two ways:

- **Codeless**: If you’re using Codeless, you will visually create the logic by dragging and dropping blocks in the logic editor. Codeless allows you to build logic without writing any code, making it accessible even for developers with minimal programming experience. You can also incorporate custom JavaScript code into Codeless if your action requires more advanced functionality.
  
- **JavaScript (Node.js)**: For developers who prefer to write code, the action’s logic can be implemented using JavaScript. This method allows for greater flexibility and is ideal for complex operations or scenarios where manual control over the logic is necessary.

In this step, you define how the action will process data, interact with other services, or perform specific calculations. The logic implemented here determines the action's behavior when it is used within a flow.

## 6. Deploy and Test Iterations
Once the logic has been added, the action needs to be thoroughly **tested** to ensure it behaves as expected. Backendless provides a testing environment where you can verify the action’s functionality. This stage is crucial to catch any errors or unexpected behavior before the action is used in FlowRunner or published to the Marketplace. The deployment process differs between services created with Codeless and Nodejs. For Codeless services, you should use the **DEPLOY MODEL** button located in the Codeless Logic Editor interface:

![deploy model button](../images/deploy-model-button.png)

For more information about FlowRunner Custom Action testing, see the [Action Testing](./action-testing.md) section of this guide.