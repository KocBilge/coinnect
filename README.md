# Coinnect

Coinnect is a modern and scalable web application designed using FastAPI, SQLAlchemy, JWT, and Celery. It provides efficient user management, authentication, and asynchronous processing functionalities.

## Project Description

Coinnect allows users to manage their accounts, perform authentication, and handle asynchronous tasks efficiently. The application offers the following core features:

- **User Registration and Management:** Enables users to create, update, and delete accounts.
- **Authentication and Authorization:** Provides secure login and access control using JWT-based authentication.
- **Asynchronous Task Management:** Utilizes Celery for handling long-running tasks in the background asynchronously.
- **Database Management:** Uses SQLAlchemy for effective management of user information and other data.

## Features

- **FastAPI:** For building fast and performant web applications.
- **SQLAlchemy:** Powerful ORM support for database operations.
- **Pydantic:** For data validation and settings management.
- **JWT (JSON Web Token):** For user authentication and authorization.
- **Celery:** For managing asynchronous tasks.
- **Redis:** For task queuing and caching.

## Installation

### Requirements

- Python 3.8 or higher
- Pip

### Setting Up Virtual Environment and Installing Packages

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    **MacOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

    **Windows:**
    ```bash
    venv\Scripts\activate
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run:

```bash
uvicorn app.main:app --reload
