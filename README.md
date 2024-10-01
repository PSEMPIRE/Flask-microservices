# Project README

## Overview
This project consists of three microservices: `dataserver`, `postserver`, and `getserver`. Each service is built using Flask and communicates with each other via HTTP requests. The `dataserver` handles data storage and retrieval, while the `postserver` and `getserver` manage item creation and retrieval, respectively.

## Prerequisites
- Docker
- Docker Compose

## Project Structure
```
├── Data
│ ├── data.py
│ └── Dockerfile
├── Getserver
│ ├── get_server.py
│ └── Dockerfile
├── Postserver
│ ├── post_server.py
│ └── Dockerfile
├── database.py
├── shared.db
├── requirements.txt
└── docker-compose.yml
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PSEMPIRE/Flask-microservices.git
   cd Flask-microservices
   ```

2. **Build and run the services using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

## Running the Project

1. **Start the services:**
   After running the above command, the services will start and be accessible at the following ports:
   - `dataserver`: `http://localhost:5002`
   - `postserver`: `http://localhost:5001`
   - `getserver`: `http://localhost:5000`

2. **Testing the Endpoints:**
   - **Add an item:**
     ```bash
     curl -X POST http://localhost:5001/ -H "Content-Type: application/json" -d '{"name": "Item Name"}'
     ```
   - **Get all items:**
     ```bash
     curl http://localhost:5000/
     ```
   - **Health check:**
     ```bash
     curl http://localhost:5001/health
     ```

## Notes
- Ensure that the `requirements.txt` file contains all necessary dependencies for the Flask applications.
- The `shared.db` file is used for SQLite database storage.

## License
This project is licensed under the MIT License.
