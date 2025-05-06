# drf-celery-redis-libraryapi
A Django REST Framework-based Library API with Celery for background task processing and Redis for caching and task queueing. Supports full CRUD, filtering, periodic tasks, and optimized caching.

## Features

- **CRUD** operations for `Book` and `Author` models
- **Filtering** of books by author name via query parameters
- **Background Task**: Archives books older than 10 years every 30 minutes using Celery
- **Caching**: Book list response cached in Redis
- **Optimized** with select_related for database performance

---

## Installed Packages

| Package              | Purpose                                          |
|----------------------|--------------------------------------------------|
| `djangorestframework`| For building RESTful APIs                        |
| `django-filter`      | For filtering support in DRF views               |
| `celery`             | Background task processing                       |
| `redis`              | Message broker for Celery & caching backend      |
| `django-celery-beat` | Periodic task scheduling                         |

Install all with:

```bash
pip install djangorestframework django-filter celery redis django-celery-beat
```
or
```bash 
pip install -r requirements.txt
```