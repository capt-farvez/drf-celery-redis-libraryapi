# Problem Statement

Design and implement a RESTful API service for an online library system using Django. The system must support full CRUD functionality for both books and authors, provide data filtering, background task processing, signal handling, and optimized database queries. It should also integrate caching mechanisms to enhance performance.

## Requirements

### 1. REST API Implementation
- Implement two models: `Author` and `Book`
- `Author`: name, date_of_birth
- `Book`: title, author (FK), published_date, genre, is_archived(False as default)
- Enable Create and Read APIs for both models using Django REST Framework
- Ensure proper serialization and validation using Django Rest Framework.

### 2. Filtering
- Allow filtering of books based on: author name
- Make the filtering available as query parameters in the GET request to the books endpoint

### 3. Background Task
- Use Celery to run a periodic task every 30 minutes
- The task sets `is_archived=True` for books older than 10 years

### 4. Caching
- Cache the list of books (GET `/books/`)
- Invalidate the cache when a book is created, updated, or deleted