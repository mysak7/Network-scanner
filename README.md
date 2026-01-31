# Network Scanner Project

A comprehensive network scanning solution with a Kubernetes-based microservices architecture, automated via GitHub Actions.

## Project Structure

```
network-scanner/
├── .github/workflows/   # CI/CD Pipeline
├── ansible/            # Infrastructure automation (K3s setup)
├── k8s/                # Kubernetes manifests
├── src/                # Source code
│   ├── scanner/        # Network scanner service
│   └── dashboard/      # Web dashboard service
├── Dockerfile.scanner  # Docker build for scanner
├── Dockerfile.dashboard # Docker build for dashboard
└── README.md
```

## Architecture

- **Scanner**: A Python service running as a CronJob that scans the network and stores results in Redis.
- **Dashboard**: A Flask web application that displays scanning statistics from Redis.
- **Redis**: Data store for scan results.
- **Infrastructure**: K3s cluster managed via Ansible, with NetBird for secure networking.

## CI/CD Pipeline

The project uses GitHub Actions for Continuous Integration and Deployment.

### Workflow: `build-deploy.yml`
1.  **Build & Push**: Builds Docker images for `scanner` and `dashboard` and pushes them to GitHub Container Registry (ghcr.io).
2.  **Deploy**: Deploys the updated images to the K3s cluster.

### Prerequisites

1.  **GitHub Secrets**:
    - `KUBECONFIG`: Base64 encoded kubeconfig file for your K3s cluster.
      ```bash
      cat ~/.kube/config | base64 -w 0
      ```

2.  **Self-Hosted Runner**:
    The deployment job runs on a self-hosted runner (recommended) or a runner with access to the K3s API.
    
    To set up a self-hosted runner on your K3s master/node:
    1.  Go to Repository Settings -> Actions -> Runners -> New self-hosted runner.
    2.  Follow the instructions to install and configure the runner.
    3.  Ensure the runner has `kubectl` installed or can access the cluster.

## Local Development

To run the components locally, you can build the Docker images:

```bash
docker build -f Dockerfile.scanner -t scanner .
docker build -f Dockerfile.dashboard -t dashboard .
```

Ensure a Redis instance is running and configured in the environment variables.
