# Scalable Python API

This repository demonstrates a structured backend service built using FastAPI. The project is intentionally organized to reflect clean architecture principles, secure authentication practices, and practical API design.

Rather than a simple CRUD example, this service models a production-style backend foundation with clear separation of concerns and layered responsibility.

---

## Architecture Overview

The application is organized into distinct layers:

- `main.py` – Application entry point and route registration
- `database.py` – Database engine and session configuration
- `models.py` – SQLAlchemy ORM models (domain layer)
- `schemas.py` – Pydantic schemas for request/response validation
- `security.py` – Password hashing utilities (bcrypt)
- `auth.py` – JWT creation and validation logic
- `routes.py` – API endpoint definitions and dependency wiring

Each component has a clearly defined responsibility to maintain clarity, testability, and scalability.

---

## Core Capabilities

- User registration with hashed password storage
- JWT-based authentication
- Token validation and protected routes
- Dependency-based authorization
- Database integration via SQLAlchemy
- Request validation using Pydantic
- Clean session management pattern

---

## Available API Endpoints

### `POST /users`
Registers a new user account.

### `POST /login`
Authenticates user credentials and returns a JWT access token.

### `GET /me`
Returns the authenticated user's profile.  
Requires a valid Bearer token.

### `GET /health`
Basic service health check endpoint.

---

## Authentication Flow

1. A user registers through `/users`.
2. Passwords are hashed using bcrypt before being stored.
3. The user logs in via `/login`.
4. A JWT access token is issued upon successful authentication.
5. Protected endpoints (such as `/me`) require a valid Bearer token.
6. The token is validated and decoded to resolve the current user context.

This approach demonstrates secure credential handling and token-based authorization using dependency injection.

---

## Technology Stack

- FastAPI
- SQLAlchemy
- Pydantic
- Passlib (bcrypt)
- Python-Jose (JWT)
- SQLite (demonstration database)

---

## Design Principles

This project emphasizes:

- Separation of concerns
- Explicit domain modeling
- Secure authentication design
- Practical backend architecture
- Readable and maintainable code

The goal is to reflect real-world backend engineering practices rather than a minimal tutorial implementation.
