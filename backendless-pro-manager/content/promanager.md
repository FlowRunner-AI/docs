Pro Manager is an integral utility in the Backendless Pro ecosystem, designed to streamline various administrative and management tasks. This utility combines multiple functions into a single, user-friendly interface, enhancing the ease of managing Backendless Pro installations. In this chapter, we'll explore the diverse capabilities of Pro Manager and how it can be leveraged for effective system management.

## Key Functions of Pro Manager
1. Backendless Pro Installation
   * Automated Setup: Simplifies the installation process of Backendless Pro, including most prerequisites, reducing manual setup efforts.
   * Environment Configuration: Configures the environment to meet the specific requirements of Backendless Pro for optimal performance.
2. License Activation
   * Easy Activation Process: Facilitates the activation of your Backendless Pro license, ensuring legal usage and access to all features.
   * License Management: Provides tools for managing and updating your license details as needed.
3. Management of Backendless Pro Components
   * Start, Stop, and Restart: Offers the ability to start, stop, or restart Backendless Pro components, giving full control over the application environment.
   * Component Control: Enables detailed management of individual components of the Backendless Pro system.
4. Viewing Logs
   * Log Access: Provides access to various logs, allowing for effective troubleshooting and monitoring of system activities.
   * Log Analysis Tools: Integrates tools for analyzing log files, aiding in quickly identifying issues or system trends.
5. Executing Upgrades
   * Upgrade Management: Streamlines the process of upgrading Backendless Pro to newer versions, ensuring your system stays up-to-date with the latest features and security updates.
   * Upgrade Notifications: Notifies users of available upgrades, keeping them informed about new releases and improvements.
6. Basic Monitoring of System State
   * System Health Check: Monitors the overall health and performance of the Backendless Pro system.
   * Real-Time Monitoring: Offers real-time insights into the system's state, including resource usage and operational status.

## Getting Started
Pro Manager is designed to simplify the management of Backendless Pro installations. This section guides you through the initial steps to get Pro Manager up and running on your system.

### Ubuntu Installation Process
To begin using Pro Manager, execute the following command in your command prompt (terminal) window:

```text
curl -o- https://raw.githubusercontent.com/Backendless/pro-manager/main/install-ubuntu.sh  | bash
```
This command performs a series of actions to download, install, and run Pro Manager on your machine.

### Windows/MacOS Installation Process
1. Ensure Node.js and NPM Installation. Confirm that Node.js and NPM (Node Package Manager) are installed on your computer. These installations are required as per the [requirements section](requirements.md).
2. Clone the Pro Manager Repository:
   * Open a command prompt or terminal window.
   * Change the current directory to the location where you wish to install Pro Manager.
   * Execute the following command to clone the Pro Manager repository:
   ```text
   git clone https://github.com/Backendless/pro-manager.git
   ```
3. Install and Launch Pro Manager:
   * Navigate to the **pro-manager** directory created in the previous step.
   * Run the following command to install the necessary dependencies:
   ```text
   npm i
   ```
   After the installation is complete, launch Pro Manager with this command:
   ```text
   npm run start
   ```
### Accessing Pro Manager UI
Once the initial part of the installation process is complete, continue setting up Pro Manager through a web browser. Point your browser to the following URL, replacing `<your-machine-ip>` with the actual IP address of your machine:

```text
http://<your-machine-ip>:5050
```

### Auxillary Installation Tasks
The installation of Pro Manager executes the following tasks on the machine where the command is run:

* User Creation: A dedicated user, `bl-pro-manager`, is created for managing Backendless Pro related operations.

* Node.js Installation: Installs Node.js version 14.18.2, providing the necessary runtime environment for Pro Manager.

* K3s Installation: Installs K3s (a lightweight Kubernetes distribution) without Traefik to manage containerized applications.

* Ingress-Nginx Installation: Installs Ingress-Nginx, facilitating network access to services running on Kubernetes.

* Project Cloning: Clones the current project into the folder /home/bl-pro-manager/pro-manager, ensuring that Pro Manager has the latest version of the necessary files.

* Service Creation: Creates the `pro-manager.service`, which manages the Pro Manager service and ensures its proper functioning.

### Pro Manager User Interface
Upon running Pro Manager for the first time, you will be guided through a series of configuration steps to install Backendless Pro. The configuration process involves the following parameters:

1. **Select Backendless Pro Version**: Choose the desired version of Backendless Pro from a drop-down list. It is recommended to select the most recent version for optimal performance and features.
2. **Local Mounting Path**: Specify a local directory that will be mounted as the root of the Backendless Pro installation. Using the default value is generally recommended for ease of setup.
3. **Backendless Pro License Key**: Enter your evaluation or permanent license key for Backendless Pro.
4. **Create a User Account for Pro Manager Access**: Set up credentials that you will use to access the Pro Manager interface.

![pro-manager-screen1](uploads/2308a4e569b890c2d9bff73230d2ffa4/pro-manager-screen1.png)

Click the **Begin Installation** button to start the Backendless Pro installation process. During installation, you will see log messages detailing the progress. Once you see the following message in the log panel:
```text
All services are created, you can see status of each service on Manage page
```
This indicates that the installation is complete, and you are ready to configure and run Backendless Pro. Click the **Manage Backendless** button to proceed:
![pro-manager-screen2](uploads/36a5917d1194ba0c90cbd20f7ebbb468/pro-manager-screen2.png)

The Manage screen provides an overview of all processes or pods that constitute the Backendless Pro installation, displaying the status of each. This user interface includes controls for stopping, starting, and restarting individual processes. Clicking on a process name opens a detailed view where you can access the process's logs and manage the process individually.:
![pro-manager-screen3](uploads/ffd36868d19f1d3644e19eed1faaf069/pro-manager-screen3.png)