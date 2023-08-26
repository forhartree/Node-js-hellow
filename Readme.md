# Node.js App Deployment to Amazon EKS

Welcome to the **Node.js App Deployment to Amazon EKS** GitHub Actions workflow. This comprehensive guide will walk you through the process of automating the deployment of a Node.js application to an Amazon Elastic Kubernetes Service (EKS) cluster using GitHub Actions. 
By the end of this guide, you'll have a deep understanding of each workflow step and its significance in the deployment process.

##Prerequisite:

1. AWS Eks Cluster.
2. AWS Cli Configure.
3. Git Hub Secrets Keys for AWS Connections.
5. If Kubernetes is configured on locally try installing Kubectl and Eksctl for interaction with Kubernetes Cluster Configuration.

## Workflow Overview

At a high level, the workflow consists of the following steps:

1. **Checkout Code**: This step ensures that the repository code is available for the workflow to operate on.

2. **Install kubectl**: We install the `kubectl` command-line tool to interact with our EKS cluster.

3. **Configure AWS Credentials**: We set up AWS credentials for secure authentication using GitHub secrets.

4. **Login to Amazon ECR**: We log in to the Amazon Elastic Container Registry (ECR) to push Docker images.

5. **Build, Tag, and Push Docker Image**: The Node.js application's Docker image is built and pushed to ECR.

6. **Update kubeconfig**: We configure `kubectl` by updating the `kubeconfig` file for EKS access.

7. **Deploy Node.js Helm Chart to EKS**: The Helm chart is deployed to the EKS cluster using Helm commands.

8. **Install and Configure kubectl**: We install `kubectl` on the runner machine for Kubernetes interaction.

## Detailed Steps

### 1. Checkout Code

The `actions/checkout` action ensures that the latest version of your repository code is available to the workflow.

### 2. Install kubectl

The `azure/setup-kubectl` action installs the `kubectl` CLI tool, allowing seamless interaction with your EKS cluster.

### 3. Configure AWS Credentials

AWS credentials are securely configured using the `aws-actions/configure-aws-credentials` action. Secrets like `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are kept safe in GitHub repository settings.

### 4. Login to Amazon ECR

The `aws-actions/amazon-ecr-login` action handles authentication to the Amazon ECR repository, ensuring secure image pushes.

### 5. Build, Tag, and Push Docker Image

The Docker image of your Node.js application is constructed, tagged as `latest`, and pushed to the Amazon ECR repository. This enables seamless deployment to the EKS cluster.

### 6. Update kubeconfig

To interact with your EKS cluster using `kubectl`, the `kubeconfig` file is updated with cluster information.

### 7. Deploy Node.js Helm Chart to EKS

Helm is used to manage Kubernetes applications. We deploy the Helm chart located in the `./node-app-chart` directory to our EKS cluster using `helm upgrade` commands.

### 8. Install and Configure kubectl

The final step installs `kubectl` on the runner machine. We download the latest stable version and place it in a directory included in the system's `PATH`.

## Workflow Triggers

The workflow is triggered by pushes to the `main` branch and pull requests targeting the `main` branch.

## Secrets

For a secure workflow, configure the following secrets in your GitHub repository settings:
- `AWS_ACCESS_KEY_ID`: AWS access key ID with appropriate permissions.
- `AWS_SECRET_ACCESS_KEY`: Corresponding secret access key.

## Workflow Benefits

This workflow streamlines the deployment process, ensuring consistency and minimizing manual intervention. It enhances collaboration among teams by automating complex deployment steps.

## Usage

1. Configure your AWS and Kubernetes permissions and settings.
2. Set up the required secrets in your GitHub repository settings.
3. Push your Node.js application code to the `main` branch.

The workflow will automatically initiate on each push, orchestrating the deployment of your Node.js app to your Amazon EKS cluster.

---

## Created Python Scripts as requested and saved under PythonScripts Folder##

