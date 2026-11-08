
# HelpDesk API

A RESTful API built using Python, FastAPI, PostgreSQL, and SQLAlchemy to manage customer support tickets.

## Project Overview

The HelpDesk API allows users to create and manage support tickets and customers. It supports ticket assignment to registered customers, ticket status updates, and database-backed CRUD operations.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn



## Features

### Ticket Management
- Create support tickets.
- Retrieve all tickets.
- Retrieve a ticket by ID.
- Update ticket details.
- Partially update ticket fields using PATCH.
- Delete support tickets.
- Manage ticket statuses: Open, In Progress, and Resolved.

### Customer Management
- Register new customers.
- Retrieve all customers.
- Retrieve customer details by ID.
- Delete customers.
- Associate tickets with registered customers.

### Database & Relationships
- PostgreSQL database integration.
- SQLAlchemy ORM for database operations.
- One-to-many relationship between customers and tickets.
- Foreign key constraint with ON DELETE SET NULL.
- Alembic database migrations.

### API Validation & Error Handling
- Pydantic request validation.
- Email validation for customers.
- HTTP 404 errors for missing records.
- Customer existence validation when creating linked tickets.



## API Endpoints

### Tickets

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tickets` | Create a ticket |
| GET | `/tickets` | Retrieve all tickets |
| GET | `/tickets/{ticket_id}` | Retrieve ticket by ID |
| PUT | `/tickets/{ticket_id}` | Update ticket details |
| PATCH | `/tickets/{ticket_id}` | Partially update a ticket |
| DELETE | `/tickets/{ticket_id}` | Delete a ticket |

### Customers

| Method | Endpoint | Description |
|---|---|---|
| POST | `/customers` | Create a customer |
| GET | `/customers` | Retrieve all customers |
| GET | `/customers/{customer_id}` | Retrieve customer by ID |
| DELETE | `/customers/{customer_id}` | Delete a customer |

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Once the application is running, visit:

http://127.0.0.1:8000/docs



## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yeshwanthreddyjannaram/helpdesk-api.git
```

### 2. Navigate to the project directory

```bash
cd helpdesk-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/helpdesk
```

Replace `YOUR_PASSWORD` with your PostgreSQL password. URL-encode special characters where necessary.

### 7. Apply database migrations

```bash
python -m alembic upgrade head
```

### 8. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs



## Project Structure

```text
HELPDESK/
│
├── app/
│   ├── routes/
│   │   ├── tickets.py
│   │   └── customers.py
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── migrations/
│   ├── versions/
│   └── env.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Future Improvements

- Add authentication and authorization.
- Add automated API tests.
- Deploy the API to a cloud platform.

## Author

Yeshwanth Reddy Jannaram

GitHub: https://github.com/yeshwanthreddyjannaram

