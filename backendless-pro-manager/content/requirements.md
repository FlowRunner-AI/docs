# Requirements

This section outlines the necessary requirements for installing and running a single (non-clustered) instance of Backendless Pro. The requirements are categorized into general prerequisites applicable to all installations and specific ones tailored to different operating systems or cloud environments.

## Instance Requirements for Optimal Performance

To successfully deploy and run the Backendless Pro Community Edition, aligning your system with the right specifications is crucial for achieving both baseline functionality and an enhanced operational experience. The guidance provided below outlines the necessary and recommended system requirements to ensure your Backendless Pro deployment is efficient and effective.

### Minimum System Requirements

Ensure your system meets the following specifications for basic functionality:

- **Memory**: A minimum of 8 GB of RAM is required to support the various operations and processes within the Backendless ecosystem effectively.
- **CPU**: At least 4 CPU cores are recommended to ensure sufficient processing power for handling multiple tasks simultaneously and maintaining overall system responsiveness.
- **Disk Space**: A minimum of 20 GB of available disk space is necessary to accommodate the initial setup and data storage needs for Backendless services and databases.

### Recommended System Specifications

For optimal performance, particularly with larger scale projects or more complex applications, consider the following system upgrades:

- **Memory**: Upgrading to 16 GB of RAM is recommended to enhance performance capabilities, enabling smoother operation of Backendless services, improved data processing, and better management of concurrent requests.
- **Disk Space Extension**: Starting with 20 GB of disk space meets the basic requirement, but the ability to expand this capacity is essential as your application and its data storage needs grow. Planning for scalable storage solutions ensures that increasing data from your application, including user data and media files, can be accommodated without impacting performance or risking data loss.

### Important Note on Configuration

It's essential to understand that these specifications serve as a guideline. The final configuration of your system should be determined in an imperative manner, through comprehensive load testing. This process involves simulating various operational loads to understand how your application performs under different conditions. Load testing will help you identify the optimal configuration that meets your specific usage patterns and requirements, ensuring that your Backendless Pro Community Edition deployment is both resilient and efficient.

By engaging in load testing, you can tailor your system's setup to match your application's demands accurately, ensuring a balance between resource availability and cost efficiency. This proactive approach allows for a customized environment that can handle your operational needs, providing a smooth and reliable experience for your users.

## Network Configuration and Port Allocation

Ensure the following ports are available on your system before installing Backendless Pro Community Edition to avoid conflicts:

{% include-markdown "./ports-description-include.md" %}

**Check Port Availability**: Use network tools or command-line utilities to confirm these ports are not used by other applications. If conflicts exist, reconfigure the conflicting applications or adjust Backendless Pro's port settings accordingly for a smooth installation.