# Solution Approach

This document outlines the design and implementation strategy for building the library API.

---

## Technologies Used

- **Django & Django REST Framework** – for API and model management
- **Celery** – for asynchronous background task handling
- **Redis** – used both as Celery broker and caching backend
- **django-celery-beat** – for periodic task scheduling

---

## Architecture Overview

- The Django project is named `library_api`
- A single app `library` manages all business logic
- API endpoints are grouped under `v1/api/`
- Models are optimized with `select_related` for DB performance
- Redis is used to store cached responses of GET `/books/`
---

## Key Components

### 1. Models
- `Author`: Contains name and date_of_birth
- `Book`: Linked to `Author`; includes title, genre, published_date, and `is_archived` flag

### 2. API Implementation
- ViewSets and Routers manage CRUD endpoints
- Serializers enforce input validation and formatting
- Filtering is supported on author name using `django-filter`

### 3. Background Task (Celery)
- Task `archive_old_books` runs every 30 mins
- Queries books older than 10 years and updates `is_archived=True`
- Task is scheduled using `django-celery-beat`

### 4. Caching Strategy
- GET `/books/` response is cached
- Cache is invalidated on create, update, or delete actions
- Cache backend is Redis