# React Flask App

A simple web application built with React.js, Python Flask and PostgreSQL.

## 📋 Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Backend Testing](#backend-testing)
  - [Frontend Testing](#frontend-testing)
  - [Inspecting Database](#inspecting-database)

## Getting Started

### Prerequisites

Ensure you have docker software installed:

- [Docker](https://docs.docker.com/engine/install/)

### Installation

1. **Clone the repository:**
    ```bash
      git clone https://github.com/kiran-machineni/ReactFlaskApp.git
    ```
2. **Navigate to the project directory:**

    ```bash
    cd ReactFlaskApp
    ```

3. **Build the Docker containers:**

    ```bash
    docker-compose up --build -d
    ```
# Usage
## Backend Testing

Test the backend by using the following curl command:
```bash
curl --location 'http://localhost:5000/add_user' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"your_username", "email":"your_email@example.com"}'
```

## Frontend Testing
Open your web browser and go to [http://localhost](http://localhost) to test the frontend.

# Inspecting Database
To inspect the PostgreSQL database, follow these steps:

1. ***Check the running Docker containers:***
   ```bash
   docker ps
    ```
2. ***Access the PostgreSQL container using its ID:***
    ```bash
    docker exec -it <your_postgres_container_id> /bin/bash
    ```
3. ***Connect to the PostgreSQL database:***
    inside the container terminal, run the following command:
    ```bash
    psql -h localhost -p 5432 -U postgres -d postgres
    ```
4. ***Inspect the database:***
    ```bash
    \dt
    ```
    ```bash
    SELECT * FROM "user";
    ```
### cleanup
Deleting the containers and volumes:
```bash
docker-compose down
```
