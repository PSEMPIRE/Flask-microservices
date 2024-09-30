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

