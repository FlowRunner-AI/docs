### Adding Let's Encrypt issuer

1. **Access the Backendless Pro Manager**:
    - Open your preferred web browser.
    - Navigate to the Backendless Pro Manager interface by entering `http://<public-ip>:5050` in the address bar. Replace `<public-ip>` with the actual public IP address of your Backendless Pro installation.

2. **Navigate to the SSL Certificate Section**:
    - In the Backendless Pro Manager, find and click on the **Configuration** tab in the top menu.
    - Select **Domains** and then choose **Ingress > Certificates**. You'll be directed to the Certificates page, which allows for the management of SSL certificates.

3. **Add a New Certificate**:
    - Click on the `Add` button to begin the process of creating a new Let's Encrypt issuer.
    - You will be prompted to provide your email address. This is for the Let's Encrypt issuer, which uses it to notify about certificate renewals and important account updates.
      
 ![](img/pro-manager-cert-page.png)

## Configuring Domain Ingress

After securing your application with an SSL certificate, the next step is to configure domain ingress settings to ensure your application is accessible and secure.

1. **Access Ingress Settings**:
    - Within the **Configuration** section of the Backendless Pro Manager, navigate to **Domains > Ingress > Ingress**.
    - This page allows you to configure how external traffic is routed to your services.

2. **Create a New Ingress Configuration**:
    - Press the `Create` button to save your new ingress configuration. This action saves the configuration to both the Backendless config values and the Kubernetes ingress.

3. **Apply Configuration**:
    - To finalize the ingress settings, press the `Apply` button. This will restart all dependent Backendless Pro services to ensure the new configuration is active.

![](img/add-api-domain-on-ingress-page.png)
   
## Verifying Server Status

Ensuring that your Backendless Pro services are up and running is crucial for the smooth operation of your application.

1. **Check Server Status**:
    - Navigate to **Server status > All** within the Backendless Pro Manager.
    - This page displays a comprehensive list of all Backendless processes and their current status.

2. **Confirm Service Availability**:
    - Wait until the status of all processes changes to **Running**. This may take a few moments as the system applies the new configurations and restarts services.