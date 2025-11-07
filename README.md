# 🚀 FastAPI CRUD Application with PostgreSQL, SQLAlchemy, and Pydantic

This project is a simple yet production-ready **FastAPI** application connected to a **PostgreSQL** database (running in Docker).
It demonstrates clean architecture using:

* SQLAlchemy ORM for database operations
* Pydantic models for validation
* Dependency Injection for DB sessions
* RESTful CRUD endpoints

---

## 🧰 Tech Stack

| Component         | Technology          |
| ----------------- | ------------------- |
| Backend Framework | FastAPI             |
| ORM               | SQLAlchemy          |
| Data Validation   | Pydantic            |
| Database          | PostgreSQL (Docker) |
| Language          | Python 3.10+        |
| Web Server        | Uvicorn             |

---

## 🐳 Run PostgreSQL Using Docker

Before starting the FastAPI app, make sure PostgreSQL is running in Docker.

```bash
docker run --name fastapi-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=fastapi_db \
  -p 5432:5432 \
  -d postgres
```

✅ This command:

* Runs PostgreSQL container named `fastapi-postgres`
* Exposes it on port **5432**
* Creates a database `fastapi_db` with username/password `postgres/postgres`

---

## ⚙️ Project Structure

```
fastapi-crud/
│
├── main.py               # FastAPI app entry point
├── models.py             # SQLAlchemy models (DB tables)
├── schemas.py            # Pydantic models (request/response)
├── database.py           # Database connection & session setup
├── crud.py               # CRUD helper functions
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---
🏃 Run the Application
```
uvicorn main:app --reload
```

Then visit:
```
🔗 API Docs: http://127.0.0.1:8000/docs

🔗 Home: http://127.0.0.1:8000/
```
📖 API Endpoints
```
Method	Endpoint	Description
GET	/	Health check
GET	/products	Get all products
GET	/products/{id}	Get product by ID
POST	/products	Create new product
DELETE	/products/{id}	Delete a product
```
