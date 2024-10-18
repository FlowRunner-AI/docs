To achieve this with GitHub Actions, you can create a workflow that triggers on merges to the main branch, connects to a VPN, installs the required Python modules, builds the MkDocs site, and copies the files to a server via SSH. Below is an example workflow configuration:

1. **Store your secrets**:
    - Add your OpenVPN credentials and configuration file as secrets in your GitHub repository.
    - Add your SSH credentials (username, server IP, and SSH private key) as secrets.

2. **Create the workflow file** (`.github/workflows/deploy.yml`):

```yaml
name: Deploy Documentation

on:
  push:
    branches:
      - main
    paths:
      - 'backendless-pro-manager/**'

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Install OpenVPN
      run: sudo apt-get update && sudo apt-get install -y openvpn

    - name: Setup OpenVPN configuration
      run: |
        mkdir -p /tmp/openvpn
        echo "${{ secrets.OPENVPN_CONFIG }}" > /tmp/openvpn/config.ovpn
        echo "${{ secrets.OPENVPN_USER }}" > /tmp/openvpn/user.txt
        echo "${{ secrets.OPENVPN_PASS }}" >> /tmp/openvpn/user.txt

    - name: Connect to OpenVPN
      run: sudo openvpn --config /tmp/openvpn/config.ovpn --auth-user-pass /tmp/openvpn/user.txt --daemon

    - name: Install Python and dependencies
      run: |
        sudo apt-get install -y python3-pip
        pip3 install mkdocs mkdocs-material mkdocs-include-markdown-plugin mkdocs-glightbox

    - name: Build MkDocs site
      working-directory: ./backendless-pro-manager
      run: mkdocs build

    - name: Copy files to server
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
        SSH_USERNAME: ${{ secrets.SSH_USERNAME }}
        SSH_SERVER: ${{ secrets.SSH_SERVER }}
      run: |
        mkdir -p ~/.ssh
        echo "$SSH_PRIVATE_KEY" > ~/.ssh/id_rsa
        chmod 600 ~/.ssh/id_rsa
        rsync -avz -e "ssh -o StrictHostKeyChecking=no" ./backendless-pro-manager/site/ $SSH_USERNAME@$SSH_SERVER:/path/to/destination
```

### Steps Breakdown:

1. **Checkout repository**: This step checks out the repository's code.
2. **Install OpenVPN**: Installs the OpenVPN package.
3. **Setup OpenVPN configuration**: Creates the necessary OpenVPN configuration files and credentials from the secrets stored in GitHub.
4. **Connect to OpenVPN**: Establishes the OpenVPN connection using the configuration and credentials.
5. **Install Python and dependencies**: Installs Python 3 and the required MkDocs modules.
6. **Build MkDocs site**: Runs `mkdocs build` in the `backendless-pro-manager` directory to build the site.
7. **Copy files to server**: Uses `rsync` over SSH to copy the built site to the server. It sets up SSH with the provided private key and disables strict host key checking for the connection.

### Storing Secrets:
- **OPENVPN_CONFIG**: The content of your `.ovpn` configuration file.
- **OPENVPN_USER**: Your OpenVPN username.
- **OPENVPN_PASS**: Your OpenVPN password.
- **SSH_PRIVATE_KEY**: Your SSH private key.
- **SSH_USERNAME**: Your SSH username.
- **SSH_SERVER**: Your SSH server address (e.g., `user@your-server.com`).

Add these secrets in your GitHub repository by navigating to `Settings -> Secrets and variables -> Actions -> New repository secret`.

This workflow should handle your requirements, connecting to the VPN, installing the necessary Python modules, building the MkDocs site, and copying the built files to your server via SSH. Adjust the server path and other configurations as necessary for your environment.