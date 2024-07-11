# azure-flask-app
This repository contains a step-by-step guide on how to deploy an e-learning course catalog website using the Azure CLI.

## Skills

- Cloud Deployment
- Web Frameworks
- Azure Cloud Services

## Prerequisites

- Basic knowledge of Azure CLI
- Basic knowledge of Azure resources
- Microsoft Azure subscription

## Technologies

- Flask
- Docker
- Azure Registry
- Azure Resource Groups

You can start the elearning Flask application by running the following command in the “App Terminal” in the `/azure-flask-app/elearning` directory:

flask run --host=0.0.0.0 --port=5000

Use the `az --version` command in the terminal to verify if the Azure CLI is installed.

## Installation Guide
- Mac Installation: `brew install azure-cli`

## Deployment Guide

### Task 1: Azure CLI Configuration
- Verify Azure CLI installation: `az --version`
- Login to Azure: `az login`
- Show current Azure account: `az account show`

### Task 2: Create an Azure Resource Group
- Create a resource group: `az group create -l eastus -n flask_app`

### Task 3: Create an Azure Container Registry
- Create a container registry: `az acr create -n flask-app-cr -g flask_app --sku Standard`

### Task 4: Build the Docker Image
- Build the Docker image: `docker build -t flaskcr.azurecr.io/flaskcr:latest .`

### Task 5: Push the Docker Image to the ACR
- Login to ACR: `az acr login --name flaskcr`
- Push Docker image: `docker push flaskcr.azurecr.io/flaskcr:latest`

### Task 6: Create an App Service Plan
- Create an App Service plan: `az appservice plan create --name flask_app_service_plan --resource-group flask_app --sku Standard`

### Task 7: Create an App Service
- Create a web app: `az webapp create --name azure-flask-e-learning --resource-group flask_app --plan flask_app_service_plan`

### Task 8: Set Up the Website Port
- Configure the web app port: `az webapp config appsettings set --resource-group flask_app --name azure-flask-e-learning --settings WEBSITES_PORT=5000`

### Task 9: Allow Admin Access to the ACR
- Enable ACR admin access: `az acr update -n flaskcr --admin-enabled true`

### Task 10: Deploy the Application
- Set up the container for the web app: `az webapp config container set --name azure-flask-e-learning --resource-group flask_app --docker-custom-image-name flaskcr.azurecr.io/flaskcr:latest --docker-registry-server-url https://flaskcr.azurecr.io`

### Task 11: Delete the Resource Group
- Delete the resource group: `az group delete -n flask_app`

## Installation Guide
- Mac Installation: `brew install azure-cli`

## Deployment Guide

### Task 1: Azure CLI Configuration
- Verify Azure CLI installation: `az --version`
- Login to Azure: `az login`
- Show current Azure account: `az account show`

### Task 2: Create an Azure Resource Group
- Create a resource group: `az group create -l eastus -n flask_app`

### Task 3: Create an Azure Container Registry
- Create a container registry: `az acr create -n flask-app-cr -g flask_app --sku Standard`

### Task 4: Build the Docker Image
- Build the Docker image: `docker build -t flaskcr.azurecr.io/flaskcr:latest .`

### Task 5: Push the Docker Image to the ACR
- Login to ACR: `az acr login --name flaskcr`
- Push Docker image: `docker push flaskcr.azurecr.io/flaskcr:latest`

### Task 6: Create an App Service Plan
- Create an App Service plan: `az appservice plan create --name flask_app_service_plan --resource-group flask_app --sku Standard`

### Task 7: Create an App Service
- Create a web app: `az webapp create --name azure-flask-e-learning --resource-group flask_app --plan flask_app_service_plan`

### Task 8: Set Up the Website Port
- Configure the web app port: `az webapp config appsettings set --resource-group flask_app --name azure-flask-e-learning --settings WEBSITES_PORT=5000`

### Task 9: Allow Admin Access to the ACR
- Enable ACR admin access: `az acr update -n flaskcr --admin-enabled true`

### Task 10: Deploy the Application
- Set up the container for the web app: `az webapp config container set --name azure-flask-e-learning --resource-group flask_app --docker-custom-image-name flaskcr.azurecr.io/flaskcr:latest --docker-registry-server-url https://flaskcr.azurecr.io`

### Task 11: Delete the Resource Group
- Delete the resource group: `az group delete -n flask_app`
