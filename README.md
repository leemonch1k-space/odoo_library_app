# Library Management Module for Odoo 18

This project is a technical assessment for an Odoo Developer position. It implements a library management system featuring book tracking, rental workflows, and a REST API.

## Features

### 1. Library Management 
* **Book Records**: Manage titles, authors, and publication dates via the `library.book` model.
* **Rental Records**: Track book loans to customers (partners) using the `library.rent` model.
* **Availability Tracking**: Automatically monitors whether a book is currently available or rented out.

### 2. Automation & Logic 
* **Rental Wizard**: A dedicated transient model (`rent.book.wizard`) to streamline the process of issuing books to clients.
* **Automated Status Updates**: When a book is rented, its `is_available` field is automatically set to `False`.
* **Data Integrity**: Python-level constraints prevent a book from being rented multiple times simultaneously if it hasn't been returned.

### 3. REST API 
* **Endpoint**: `GET /library/books`.
* **Functionality**: Returns a JSON object containing all books, including their current availability status.

## Technical Stack
* **Framework**: Odoo 18 Community.
* **Database**: PostgreSQL 17.
* **Deployment**: Docker & Docker Compose.

## Installation & Setup

1.  **Environment Configuration**: Ensure the `.env` file is present in the root directory with the following database credentials:
    * `POSTGRES_DB=test_odoo`
    * `POSTGRES_USER=odoo`
    * `POSTGRES_PASSWORD=password`

2.  **Launch the Environment**: Run the following command to start Odoo and PostgreSQL:
    ```bash
    docker compose up -d
    ```

3.  **Module Activation**:
    * Access Odoo at `http://localhost:8069`.
    * Log in and **Activate Developer Mode** in the settings.
    * Go to the **Apps** menu, search for `library_management`, and click **Activate**.

## Development Standards
* **Code Documentation**: The source code is extensively commented to explain the logic and ORM methodology used, as per the project requirements.
* **Structure**: Follows standard Odoo module architecture including `models/`, `views/`, `wizard/`, `security/`, and `controllers/`.

---
*Developed as part of an Odoo Developer Technical Assessment.*