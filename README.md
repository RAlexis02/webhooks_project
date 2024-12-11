# webhooks_project

# Webhooks Project

![Project Screenshot](https://via.placeholder.com/1200x400.png?text=Webhooks+Project)

Welcome to the **Webhooks Project**! This is a simple Python-based web application that demonstrates the usage of webhooks. The application runs on Flask and is fully containerized using Docker, making it easy to deploy and run.

---

## Features
✨ Lightweight Flask application.  
🔗 Accepts webhook POST requests.  
🐋 Fully Dockerized for quick deployment.  
📄 Easy setup and usage instructions.  

---

## Requirements
To use or test this project, ensure you have the following:

1. **Docker Installed:**
   - Download and install Docker from the [official Docker website](https://www.docker.com/products/docker-desktop).
   - Confirm Docker is running by opening Docker Desktop.

2. **Verify Installation:**
   ```bash
   docker --version
If Docker is correctly installed, this command will display the installed version.

How to Run
Option 1: Pull and Run from Docker Hub
Pull the Docker Image:

bash
Copiar código
docker pull rommela462/container.3
Run the Docker Container:

bash
Copiar código
docker run -d -p 5000:5000 rommela462/container.3
-d: Runs the container in detached mode.
-p 5000:5000: Maps port 5000 on your local machine to port 5000 inside the container.
Access the Application: Open your browser and navigate to:

arduino
Copiar código
http://localhost:5000
The application should display: "Hello, Webhooks!"

Test the Webhook Endpoint: Use Postman or curl to send a POST request:

bash
Copiar código
curl -X POST -H "Content-Type: application/json" -d '{"example":"data"}' http://localhost:5000/webhook
Option 2: Build Locally and Run
Clone the Repository:

bash
Copiar código
git clone https://github.com/RAlexis02/webhooks_project.git
cd webhooks_project
Build the Docker Image:

bash
Copiar código
docker build -t rommela462/container.3 .
Run the Container:

bash
Copiar código
docker run -d -p 5000:5000 rommela462/container.3
Test the Application:
Same as in Option 1.

Option 3: Using Docker Compose
Ensure docker-compose.yml is Present:

yaml
Copiar código
version: "3.8"
services:
  webhooks:
    build: .
    ports:
      - "5000:5000"
Start the Application:

bash
Copiar código
docker-compose up --build
Stop the Application:

bash
Copiar código
docker-compose down
Project Structure
bash
Copiar código
webhooks_project/
├── app.py             # Main application file
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Optional, for Docker Compose
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
Testing the Application
Open your browser and navigate to http://localhost:5000.
You should see "Hello, Webhooks!".

Test the /webhook endpoint using curl:

bash
Copiar código
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:5000/webhook
Troubleshooting
Docker Not Running
Ensure Docker Desktop is open and running before executing any Docker commands.

Port Conflict
If port 5000 is already in use, modify the port mapping:

bash
Copiar código
docker run -d -p 8080:5000 rommela462/container.3
Access the application at http://localhost:8080.

Permission Issues
On some systems, you may need to prefix commands with sudo:

bash
Copiar código
sudo docker run -d -p 5000:5000 rommela462/container.3
License
This project is open-source and available under the MIT License.