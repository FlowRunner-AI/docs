# Installing Backendless PRO on Ubuntu

The simplest way to install Backendless PRO on Ubuntu is to execute the following command in the terminal:

```
{% include-markdown "./ubuntu-install-command-include.md" %}
```

This command performs several important tasks to set up your Backendless PRO environment:

1. **Creates `bl-pro-manager` User**: An Ubuntu user named `bl-pro-manager` is created to manage the Backendless PRO installation.

2. **Installs Kubernetes (k3s)**: A lightweight Kubernetes distribution called `k3s` is installed under the `bl-pro-manager` user. Kubernetes is essential for managing and orchestrating the containerized services that make up Backendless PRO.

3. **Installs Node.js 14**: Node.js version 14 is installed, providing the necessary runtime for running various Backendless PRO services and scripts.

4. **Clones and Runs PRO Manager**: The command clones the PRO Manager repository and runs it. The PRO Manager is responsible for managing and orchestrating the Backendless PRO services, ensuring they run smoothly and are properly configured.

### Summary

By executing the provided command, you can easily set up Backendless PRO on your Ubuntu system. This command automates the creation of a dedicated user, installation of necessary components like Kubernetes `k3s` and Node.js 14, and initializes the PRO Manager, making the installation process straightforward and efficient.