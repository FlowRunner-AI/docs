This section outlines the necessary requirements for installing and running a single (non-clustered) instance of Backendless Pro. The requirements are categorized into general prerequisites applicable to all installations and specific ones tailored to different operating systems or cloud environments.

## General Requirements
Before proceeding with the installation of Backendless Pro, ensure that your system meets the following general requirements:

* **Memory**: At least 8 GB of RAM.
* **CPU**: 4 CPU cores.
* **Disk Space**: A minimum of 20 GB available disk space.
These requirements are essential to ensure optimal performance and stability of Backendless Pro.

The installation will utilize the following ports. Make sure no other application uses the ports to avoid a conflict:
* 5050 - Pro Manager web server for the User Interface
* 5051 - Pro manager web socket for real-time log streaming and other updates
* 32300 - Backendless API endpoint
* 32400 - Backendless Console web server
* 32600 - [Consul](consulconfig.md) (configuration values)

## Specific Requirements
### For Ubuntu Users
For users operating on Ubuntu or other Debian-based systems, the [Backendless Pro Manager](promanager.md) significantly simplifies the installation process. This tool is specifically designed to automate the installation of all necessary prerequisites, streamlining the setup of Backendless Pro on your system. Continue the installation by following the [Pro Manager](promanager.md) instructions.

### For Windows and MacOS Users
If you are on Windows or MacOS start with the instructions below. Once these steps are completed, proceed to the General Prerequisites section.
1. **Docker Desktop Installation**: Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop/). Docker Desktop provides the necessary environment for running containerized applications on MacOS and Windows.
2. **Enable Kubernetes**: Open Docker Desktop. Navigate to the Preferences or Settings menu.
Locate the Kubernetes section and select the `Enable Kubernetes` checkbox. A screenshot illustrating this step:![enable-kuber](uploads/e3ef7cd5b7cb9bdfdb21376dabee4e1f/enable-kuber.png)

## General Prerequisites
1. **Install node v14.18.2**: You can find installation instructions specific to your operating system on the [NVM's github page](https://github.com/nvm-sh/nvm). Generally, the following command should work for most environments:
   ```text
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash \
      && source ~/.bashrc \
      && nvm install v14.18.2
   ```
2. Verify that the install/current version of node on your machine is 14.18.2 by running the following command:
   ```text
   node -v 
   ```
3. **Install K3S**: Skip this step if you installed Docker Desktop.
   ```text
   curl -sfL https://get.k3s.io | sh - \
     && mkdir ~/.kube \
     && echo "export KUBECONFIG=~/.kube/config" >> ~/.bashrc \
     && source ~/.bashrc \
     && sudo k3s kubectl config view --raw > "$KUBECONFIG"
     && kubectl get nodes
   ```
4. **Verify kubectl**: Make sure that you have access to `kubectl`. Execute the following command to confirm:
   ```text
   kubectl get nodes
   ```
   You should receive a response similar to the following, indicating a successful Kubernetes setup:
   ```text
   username@machinename:~/pro-manager$ kubectl get nodes
   NAME             STATUS   ROLES                  AGE   VERSION
   machinename      Ready    control-plane,master   19h   v1.24.3+k3s1 
   ```
5. **Install ingress**: See the [Quick Start guide](https://kubernetes.github.io/ingress-nginx/deploy/#quick-start) or use the command below. 
   ```test
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
   ```
6. **Install cert-manager**.
   ```text
   kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
   ```

After all the prerequisites are installed, continue the installation by following the [Pro Manager](promanager.md) instructions.

## For Cloud Environments
[Instructions for specific cloud environments like AWS, Google Cloud, Azure, etc., can be added here]