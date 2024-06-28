Backendless PRO provides two primary methods for configuration: environment variables and Consul key-value storage. These options offer flexibility and control, catering to different deployment needs. Understanding how to use these methods and their precedence is crucial for effective configuration.

### Configuration Order of Precedence

When setting up Backendless PRO, it is important to know which configuration sources take priority:

1. **Environment Variables**: These have the highest priority. Any settings specified here will override those in Consul.
2. **Consul Key-Value Storage**: Acts as a centralized store for configuration but can be overridden by environment variables.

### Using Environment Variables

Environment variables are a simple and effective way to configure Backendless PRO, especially within a Kubernetes environment. To override a Consul setting with an environment variable, follow this naming pattern:

```
BL_PROPERTY_<key-from-consul>
```

#### Example: Overriding Consul Values

Suppose you need to change the `reservedApplications` setting in Consul. You would set an environment variable in your Kubernetes configuration as follows:

```bash
BL_PROPERTY_config_application_reservedApplications=20
```

This will set the `reservedApplications` value to `20`, taking precedence over the value stored in Consul.

### Using Consul for Configuration

Consul provides a centralized method to manage your Backendless PRO configurations. It is especially useful for more complex setups where maintaining a single source of truth is beneficial.

#### Direct Access to Consul

You can directly access the Consul UI using the following URL format, replacing `<your-public-ip>` with your actual public IP address:

```
http://<your-public-ip>:32600
```

This allows you to view and manage your configuration settings directly within the Consul interface.

#### Secure Access through Pro Manager

For a more secure and controlled approach, access Consul through the Backendless Pro Manager. This tool allows you to set up a domain with authentication credentials, ensuring secure access to your configuration data.

1. **Log In to Pro Manager**: Use your administrator credentials.
2. **Configure the Domain**: Set up the domain for accessing Consul, including user authentication.
3. **Manage Port Access**: Enable or disable port 32600 to control direct access to Consul.

### Summary

Backendless PRO offers robust configuration options through environment variables and Consul. By understanding the order of precedence and how to utilize each method, you can efficiently manage your Backendless PRO setup, ensuring a flexible, secure, and well-organized deployment.