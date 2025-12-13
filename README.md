# Practica-Microservicios-azure

This project is a microservices architecture implemented using Docker and Azure. It consists of several services that work together to provide a complete application. Below is a brief overview of each component.

## Services

### Auth Service
- **Location:** `auth_service/`
- **Description:** This service handles user authentication, including registration, login, and token management.
- **Main File:** `app.py`
- **Dependencies:** Listed in `requirements.txt`
- **Dockerfile:** Contains instructions to build the Docker image for the auth service.

### Game Service
- **Location:** `game_service/`
- **Description:** This service manages game-related operations, such as creating, updating, and retrieving game data.
- **Main File:** `app.py`
- **Dependencies:** Listed in `requirements.txt`
- **Dockerfile:** Contains instructions to build the Docker image for the game service.

### Score Service
- **Location:** `score_service/`
- **Description:** This service manages scores, allowing users to submit and retrieve scores.
- **Main File:** `app.py`
- **Dependencies:** Listed in `requirements.txt`
- **Dockerfile:** Contains instructions to build the Docker image for the score service.

### Frontend
- **Location:** `frontend/`
- **Description:** This is the user interface of the application, built using HTML.
- **Main File:** `index.html`
- **Dockerfile:** Contains instructions to build the Docker image for the frontend application.

## Docker Compose
- **File:** `docker-compose.yml`
- **Description:** This file defines the services, networks, and volumes for the multi-container Docker application. It specifies how to build and run each service.

## Azure Integration
- **File:** `azure-pipelines.yml`
- **Description:** This file defines the Azure DevOps pipeline configuration for continuous integration and deployment. It specifies the steps to build and deploy the application to Azure.

## Infrastructure
- **Location:** `infra/`
- **Files:**
  - `main.bicep`: Bicep template for deploying Azure resources.
  - `parameters.json`: Provides parameters for the Bicep template.

## Development
- **.dockerignore:** Specifies files and directories to ignore when building Docker images.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Build the Docker images using Docker Compose:
   ```
   docker-compose up --build
   ```
4. Access the services via the specified ports.

## Usage
- The application can be accessed through the frontend, which communicates with the backend services for authentication, game management, and score handling.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.