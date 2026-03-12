# Text Intelligence API

Backend service built with FastAPI that provides authenticated endpoints for user management and AI-assisted text analysis. The API exposes endpoints for registration, authentication, profile access, and text analysis, returning structured insights such as summary, keywords, and sentiment.

---

## Service Structure

The codebase is organized into focused modules:

* **main.py** – Application entry point and router registration
* **database.py** – SQLAlchemy engine and session configuration
* **models.py** – ORM models representing application entities
* **schemas.py** – Pydantic schemas used for request and response validation
* **security.py** – Password hashing utilities (bcrypt)
* **auth.py** – JWT generation and authentication helpers
* **routes.py** – API endpoints and dependency wiring
* **ai_service.py** – Integration with an external AI model for text analysis

---

## API Endpoints

**POST /users**
Create a new user account.

**POST /login**
Authenticate a user and return a JWT access token.

**GET /me**
Return the authenticated user profile.
Requires a valid Bearer token.

**POST /ai/analyze**
Analyze input text and return structured insights including summary, keywords, and sentiment.
Requires authentication.

**GET /health**
Basic service health check endpoint.

---

## Authentication

Authentication is handled using JSON Web Tokens (JWT).
Passwords are hashed with bcrypt before being stored.
Protected routes resolve the authenticated user through dependency injection.

---

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Passlib (bcrypt)
* Python-Jose (JWT)
* OpenAI API
* SQLite
