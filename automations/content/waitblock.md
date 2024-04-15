### Implementing Delays

Introducing pauses or delays in your automation flows can be crucial for timing certain actions perfectly. Imagine you want to send a welcome email to a new user after they register for your service. To avoid sending it instantly and to make the process feel more personalized, you might decide to delay the email delivery. Backendless makes this easy with the `Wait` block, allowing you to incorporate such pauses seamlessly into your flows.

### Why `Wait`?

The `Wait` block serves a simple yet powerful purpose: it pauses the flow of actions for a specified period. This feature can be handy in various scenarios, such as delaying notifications, emails, or any other actions, to ensure they occur at the most opportune moment.

### Setting Up Delays

The `Wait` block offers two approaches for injecting a delay in the flow execution. Each approach is designed to meet different needs:

- **Simple Mode**: For direct and uncomplicated delays, the Simple Mode lets you specify a fixed delay in days, hours, minutes, or seconds. This mode is ideal when you need a consistent pause in your flow. The requirement is to set at least one of these time units to a non-zero value.
![simple mode wait block](images/wait-block-simple-mode.png)

- **Advanced Mode**: For scenarios where the delay needs to be more flexible, the Advanced Mode comes into play. This mode utilizes the Expression Editor, which allows you to calculate the delay period dynamically. Whether through a variable, a property, or a custom expression, the resulting value determines the length of the pause, measured in seconds.

### Key Insights

Implementing delays in Backendless automation flows offers a straightforward method to time your actions precisely, enhancing the overall effectiveness and personalization. Whether you're aiming for simplicity with a fixed delay or seeking flexibility with dynamic calculation, the `Wait` block provides the necessary functionality to integrate these pauses into your flows effortlessly.
