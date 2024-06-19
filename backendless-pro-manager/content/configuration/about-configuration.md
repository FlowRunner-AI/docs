# Configuration Options
Backendless Pro leverages Consul by HashiCorp as a distributed key-value storage system for platform configuration. Additionally, you can override default configuration settings using environment variables. These methods offer flexibility and control to suit different deployment needs. Understanding their usage and precedence is crucial for effective configuration. The Environment Variables option has higher order of precedence. Any settings specified in the variables will override those in Consul. 

## Using Environment Variables

Environment variables are a simple and effective way to configure Backendless Pro, especially within a Kubernetes environment. To override a Consul setting with an environment variable, follow the following naming pattern:

```
BL_PROPERTY_<key-from-consul>
```

Suppose you need to change the `reservedApplications` setting in Consul. You would set an environment variable in your Kubernetes configuration as follows:

```bash
BL_PROPERTY_config_application_reservedApplications=20
```

This will set the `reservedApplications` value to `20`, taking precedence over the value stored in Consul.

## Using Consul for Configuration

Consul provides a centralized method to manage your Backendless Pro configurations. It is especially useful for more complex setups where maintaining a single source of truth is beneficial.

### Direct Access to Consul

You can directly access the Consul UI using the following URL format, replacing `<your-public-ip>` with your actual public IP address:

```
http://<your-public-ip>:32600
```

This allows you to view and manage your configuration settings directly within the Consul interface.

### Secure Access through Pro Manager

For a more secure and controlled approach, access Consul through the Backendless Pro Manager. This tool allows you to set up a domain with authentication credentials, ensuring secure access to your configuration data.

1. **Log In to Pro Manager**: Use your administrator credentials.
2. **Configure the Domain**: Set up the domain for accessing Consul, including user authentication.
3. **Manage Port Access**: Enable or disable port 32600 to control direct access to Consul.

## Summary

Backendless Pro offers robust configuration options through environment variables and Consul. By understanding the order of precedence and how to utilize each method, you can efficiently manage your Backendless Pro setup, ensuring a flexible, secure, and well-organized deployment.