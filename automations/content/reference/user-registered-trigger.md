The "User Registered" trigger block in FlowRunner™ is designed to pause a flow until a new user account is created within your Backendless application. This trigger is activated when the [user registration API](https://backendless.com/docs/rest/users_user_registration.html) call is used, which means a user uses the registration form in your application or someone with admin privileges registers a user.

## Trigger Properties
The trigger properties include:

* **Name** - should be a meaningful name that represents what this trigger does. Follow the recommendations in the [Block Naming](../flow-editing/blocknaming.md) section of this guide for best practices.
* **Condition** - an optional condition associated with the trigger. When the trigger receives an activation event (i.e. when a user is being registered with the API), the system checks the condition. If the condition is evaluated to `TRUE`, the flow execution proceeds, otherwise, the trigger's event is ignored.
* **Reference Trigger Data As** - this is a name assigned to the data that activated the trigger. The data is a key/value structure that contains the values from the user registration API call.

![user registration block](../images/user-registration-block.png)


## Assigning Custom Name
To make your workflow more intuitive, it's recommended that you rename this block to something that clearly reflects the specific part of the process you are automating. Any references to the trigger activation event in the Expression Editor will then use this new name, which helps keep your workflow organized and understandable. The data received upon trigger activation can be utilized in any subsequent blocks within the flow. For example, the screenshot above shows the block has a name of `User Registered via Form`. Notice that in the screenshot below, the data for the trigger activation event uses the assigned name.

## Accessing Trigger Data
Once activated, the trigger event provides the new user’s information in a key/value structure format. The keys in this structure correspond to the column names in Backendless' "Users" table, and the values are what were included in the user registration API call.

![user registration data](../images/user-registration-data.png)

???+ note
    One crucial detail to remember is that if a user is created directly through the Backendless Console, this trigger will not activate since the User Registration API call isn't utilized in that scenario.

## Conditional Trigger Activation
The "User Registered" trigger block also supports conditional logic. You can set conditions that control whether the trigger activates when a user registers. For the trigger to proceed, the condition must evaluate to true. More details on configuring these conditions can be found in the ["Conditional Logic"](../flow-editing/conditions.md) chapter of this guide.