### For Windows and MacOS Users
If you are on Windows or MacOS start with the instructions below. Once these steps are completed, proceed to the General Prerequisites section.

1. **Docker Desktop Installation**: Download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop/). Docker Desktop provides the necessary environment for running containerized applications on MacOS and Windows.
2. **Enable Kubernetes**: Open Docker Desktop. Navigate to the Preferences or Settings menu.
   Locate the Kubernetes section and select the `Enable Kubernetes` checkbox. 

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
