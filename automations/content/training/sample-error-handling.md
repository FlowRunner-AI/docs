# Sample Error Handling Flow  

The **Sample Error Handling Flow** demonstrates how to implement error handling in FlowRunner™. It is a comprehensive example showcasing how to log progress and errors using FlowLogger, handle errors gracefully with `Handle Error` blocks, and process data through conditional logic. This flow is ideal for understanding how to build robust workflows that can recover from unexpected issues.  

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/0gwQZy42moI?si=yGgLGFPw_SpgjwNe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## How the Flow Works  

The flow starts with an **External Callback** trigger (labeled as **Data For New Task**). This trigger is activated when its unique endpoint URL is invoked. 

![initial trigger in sample flow](../images/sample-flow-initial-trigger.png)

The flow expects four parameters in the URL:  

- **Description**: A brief description of the task.  
- **Done**: A boolean value indicating whether the task is completed.  
- **Due**: A timestamp for the task's due date.  
- **Responsible User Email**: The email address of the person responsible for the task.  

Once activated, the trigger passes the parameters into the flow. The first action logs the incoming data to FlowLogger for transparency and debugging.  

![log incoming data](../images/sample-flow-log-incoming-data.png)

After logging the input, the flow saves the task details into the **Tasks** database table. This table has columns corresponding to the provided parameters. If the save operation is successful, a success message is logged to FlowLogger, otherwise, if there is an error with saving the data in the database, the flow is routed to the **Create Task Error** block, which is an error handler. The flow then logs the error in FlowLogger.

![database error handling](../images/sample-flow-db-error-handling.png)

Next, the flow sends a notification email to the email address specified in the `Responsible User Email` parameter. This email informs the user that a new task has been created in the database. The flow logs a message upon successful email delivery.  

![email delivery action](../images/sample-flow-email-action.png)

Finally, the flow updates the database record for the task, marking it as having sent the notification email.  

## Error Handling  

The flow is designed to handle errors at critical points, specifically during the database save and email sending tasks. If either task fails, the associated `Handle Error` block redirects the flow to a logging action. This action sends the error details to FlowLogger, ensuring you have the information needed to diagnose and fix the issue.  

## Execution Prerequisites  

Before running the flow, ensure you have completed the following setup steps:  

1. **Configure FlowLogger**  
   Open [FlowLogger](https://logger.flowrunner.ai) in a separate browser window. Note the session code displayed on the screen. In the Flow Editor, select any **Log...** block, click the **Configure** button in the properties panel, and enter the session code. Save your changes to link the block to FlowLogger.  

2. **Set Up Gmail Integration**  
   Select the **Send User Notification** block in the flow. Click the **Login** button in the properties panel and follow the prompts to log in with your Google credentials. This step authorizes the flow to send emails using your Gmail account.  

## Running the Flow  

To start the flow, click the **Start Flow** icon in the Flow Editor. The flow begins when its **External Callback** trigger (labeled as **Data For New Task**) is activated.  

### Accessing the Trigger URL  

You can get the trigger URL in two ways:  

- Select the **Data For New Task** block in the Flow Editor and find the URL there.  
- Alternatively, open the flow version description in the Flow Manager, where the full URL is listed.  

The complete URL includes placeholders for all required parameters:  

``` { .js .copy }
https://[YOUR APP HOSTNAME]
    /api/automation/flow/C4C5E4E4-E412-4CBC-8758-24E5AF547FBB/trigger/B66A837A-2C9C-87CE-45D5-10A4A66EEC46/activate?
    Description=CreatedByFlowRunner™Trigger&
    Done=false&
    Due=1732140000000&
    Responsible%20User%20Email=youremailexample@gmail.com
```  

### Running the Flow  

Copy the URL into your browser and replace `[YOUR APP HOSTNAME]` with the appropriate hostname for your Backendless app. Ensure all required parameters are included. When the URL is executed correctly, the flow will:  

1. Log the incoming parameters.  
2. Save the task to the database.  
3. Send a notification email to the specified user.  
4. Update the task record to indicate the notification was sent.  

If any parameters are missing or invalid, the flow triggers an error. For example, try the following scenarios and observe how the flow handles the errors:

* Omit the value for the `Responsible User Email` parameter or providing a poorly formatted email address
* Specify an invalid date value for the  `Due` argument. (for example, `abc`)
* Specify a wrong parameter name. (for example, `Responsible User Email1`)
