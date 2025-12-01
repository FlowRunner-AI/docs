The **Assign Instance Name** action in FlowRunner™ enables flow designers to dynamically assign a unique and descriptive name to each flow instance. This name acts as a visual identifier in the analytics interface, enhancing traceability and making it easier to interpret execution data.  

Every flow instance operates in its own isolated context, managing the data specific to that instance. Assigning an instance name provides a meaningful label in analytics, allowing flow designers to quickly identify and analyze individual runs, especially when multiple instances execute concurrently.  

### How It Works  

Flow designers use the [Expression Editor](../flow-editing/expressioneditor.md) to define the name for an instance. This name can be dynamically generated using: 

- Data from trigger events.  
- Outputs from actions and transformations.  
- Static text combined with dynamic values.  

For example, a flow processing customer feedback might use the following name:  
```
User: {{User Name}}, Email: {{Email Address}}
```
where `User Name` and `Email Address` are values retrieved earlier in the flow.  

### Timing of Name Assignment  

It is recommended to assign the instance name early in the flow's runtime. Analytics will display the name only after it has been assigned. If the flow runs for an extended period before the name is set, its analytics entry will show a unique identifier assigned buy the system. Assigning the name at the start (or right after start) ensures visibility throughout the entire lifecycle of the flow instance.  

### Setting Up  

To configure the **Assign Instance Name** action:  

1. **Add the Action**: Place the **Assign Instance Name** block in the flow at the point where the name should be assigned. Ideally, this should be near the beginning of the flow.  
2. **Define the Name**: Use the **Expression Editor** to create a meaningful name. You can use:  

     - A single dynamic value, such as `{{UserEmail}}`.  
     - A composite value, such as `Feedback Submission - {{FeedbackID}}`.  
     - A combination of multiple data points to provide detailed context.  

3. **Save the Configuration**: Once the configuration is complete, the action will assign the specified name to the flow instance when executed.  

### Best Practices  

- **Leverage Dynamic Names**: Use the flexibility of the [Expression Editor](../flow-editing/expressioneditor.md) to create meaningful and unique names that reflect the flow’s context.  
- **Assign Early**: Place the **Assign Instance Name** block early in the flow to ensure the instance is identified in analytics from the start.  
- **Be Descriptive**: Choose names that provide insight into the instance's purpose or key data to simplify monitoring and debugging.  

By using the **Assign Instance Name** action effectively, flow designers can enhance the transparency and manageability of their flows while improving the usefulness of analytics.  