# Flask Microservices with Docker

This repository contains a set of microservices built using Flask and Docker. The microservices communicate with each other, where one service is responsible for handling GET requests and another handles POST requests. The data is stored in an SQLite database.

## Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [API Endpoints](#api-endpoints)

## Architecture

This project follows a microservices architecture with three main components:

1. **Get Server (localhost:5000)**: Handles GET requests to retrieve items.
2. **Post Server (localhost:5001)**: Handles POST requests to add new items.
3. **Data Server (localhost:5002)**: Interacts with the shared SQLite database for CRUD operations.

Each of these services runs inside its own Docker container and communicates over HTTP.

## Prerequisites

Before running the project, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Project Structure
├── Data/
│   ├── data.py               # Contains functions to interact with the database (GET, POST)
│   └── Dockerfile            # Dockerfile to build the Data microservice container
├── Getserver/
│   ├── get_server.py         # Flask server to handle GET requests, communicates with Data microservice
│   └── Dockerfile            # Dockerfile to build the Getserver microservice container
├── Postserver/
│   ├── post_server.py        # Flask server to handle POST requests, communicates with Data microservice
│   └── Dockerfile            # Dockerfile to build the Postserver microservice container
├── database.py               # SQLAlchemy models and database connection setup
├── shared.db                 # SQLite database file (automatically created if not present)
├── requirements.txt          # Contains Python package dependencies required for the microservices
├── docker-compose.yml        # Docker Compose file to orchestrate the containers for each microservice
├── .gitignore                # Specifies files and directories to be ignored by git (e.g., shared.db)
└── README.md                 # Documentation file with instructions on setting up and running the project


## How to Run

Follow these steps to set up and run the microservices:

### 1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


### 2. Build and Run the Containers
docker-compose up --build

### 3. API Endpoints
GET http://localhost:5000/
POST curl http://localhost:5001/

### 4. Stop the Services
docker-compose down

### 5. Cleaning Up
docker-compose down --rmi all --volumes --remove-orphans


### Troubleshooting
Connection Issues: Ensure that the services are running, and the ports (5000, 5001, and 5002) are not being used by any other processes.
Database Issues: If there's an issue with the database, delete shared.db and restart the services. The database will be recreated.
