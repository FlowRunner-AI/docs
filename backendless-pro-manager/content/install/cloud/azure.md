# Install Backendless PRO in Microsoft Azure

This installation guide provides step-by-step instructions on setting up Backendless PRO on a Microsoft Azure virtual machine running Ubuntu. Before you begin the installation, ensure that your Azure instance meets the necessary [requirements](../../requirements.md) to support Backendless PRO.

## Prerequisites
- An active Microsoft Azure account.
- Basic knowledge of cloud server management and Ubuntu.

## Step-by-Step Installation Guide

### Step 1: Set Up Your Azure Virtual Machine
1. Log in to your Microsoft Azure portal.
2. Create a new virtual machine (VM) configured with Ubuntu. Refer to Azure's documentation for details on VM creation.
3. During the VM setup, include the following script in the **User Data** section to automatically install necessary components on your Ubuntu server:

    ```bash
    #!/bin/bash
    {% include-markdown "../ubuntu-install-command-include.md" %}
    ```

### Step 2: Configure Necessary Ports
Ensure the following ports are open and available on your VM, as Backendless requires these ports for proper operation:

{% include-markdown "../../ports-description-include.md" %}

### Step 3: Access the Backendless Pro Manager
{% include-markdown "../access-pro-manager-include.md" %}

### Step 4: Install Backendless PRO

Upon accessing the Backendless PRO Manager, you will be presented with a setup form. Complete the form to start the installation process of Backendless PRO. This setup will configure Backendless PRO to operate with your Azure instance specifics.

Once the installation is completed, you will be able to use Backendless PRO on your Azure instance. For further operations or troubleshooting, refer to the specific sections of the Backendless documentation or contact support if you encounter issues beyond the setup scope.

### Step 5: Domain configuration
To set up domains for your newly installed Backendless instance, follow the guidelines provided in the [Azure Load Balancer documentation](./azure-load-balancer.md).

### Step 6: Create a Backendless Account and Your First App
1. Register for a new account within the Backendless Console.
2. Create your first application. This marks the completion of the Backendless installation on your Azure VM.
