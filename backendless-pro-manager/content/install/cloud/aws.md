# Installing Backendless PRO on AWS EC2

This guide provides detailed instructions on how to install Backendless PRO on an AWS EC2 instance running Ubuntu. Ensure that you start by selecting the correct EC2 instance type according to the [requirements](../../requirements.md).

### Step 1: Launch an EC2 Instance

Begin by starting an EC2 instance with Ubuntu as the operating system. During the setup, use the following `User data` script to automate the installation prerequisites. Copy and paste the script into the `User data` section:

```bash
#!/bin/bash
{% include-markdown "../ubuntu-install-command.md" %}
```

Refer to the image below to locate where to input the `User data` during the EC2 instance setup:

![EC2 Launch Instance](img/EC2-launch-instance.png)

### Step 2: Wait for the Instance to Become Available

Once the instance has been initiated, wait until it is fully operational. You can check the status on your AWS EC2 dashboard. When the instance is ready, it should display as available, and you should take note of the public IP address or URL provided by AWS.

Make sure the following ports are available:

{% include-markdown "../../ports-description.md" %}

![EC2 Instance Ready](img/EC2-ready.png)

### Step 3: Access Backendless PRO Manager

With the public IP or URL:

1. Open a web browser.
2. Navigate to `http://<your-public-ip>:5050`. Replace `<your-public-ip>` with the actual public IP address of your EC2 instance.

This URL will direct you to the Backendless PRO Manager.

### Step 4: Install Backendless PRO

Upon accessing the Backendless PRO Manager, you will be presented with a setup form. Complete the form to start the installation process of Backendless PRO. This setup will configure Backendless PRO to operate with your EC2 instance specifics.

Once the installation is completed, you will be able to use Backendless PRO on your AWS EC2 instance. For further operations or troubleshooting, refer to the specific sections of the Backendless documentation or contact support if you encounter issues beyond the setup scope.