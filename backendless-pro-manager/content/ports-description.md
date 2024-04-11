- **5050**: This port is dedicated to the Pro Manager web server, which hosts the User Interface (UI). The UI is a critical component for managing and configuring your Backendless environment, providing a graphical interface for ease of operation.

- **5051**: Utilized by the Pro Manager for web socket connections, this port enables real-time log streaming and other dynamic updates. This feature is vital for live monitoring of your application's performance and behavior, facilitating immediate responsiveness to events as they occur.

- **32300**: Designated for the Backendless API endpoint, port 32300 is a primary communication channel for your applications to interact with the Backendless services. Ensuring this port is open and conflict-free is essential for the seamless operation of your application's backend functionalities.

- **32400**: This port serves the Backendless Console web server, which is an administrative interface for the Backendless platform. Through the console, users can access a wide range of tools and settings for application management, analytics, and more.

- **32600**: Dedicated to Consul, which is used for [managing configuration values](consulconfig.md) within the Backendless ecosystem. Consul plays a critical role in service discovery and configuration, making this port essential for the coherent operation of distributed services and microservices within your Backendless deployment.
