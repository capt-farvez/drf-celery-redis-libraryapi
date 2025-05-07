# Setup celery for background task
These functions are for my project. Please edit your as required.

### 1. Install Required Packages
```
pip install celery redis django-celery-beat
```
**Add django_celery_beat to your INSTALLED_APPS in settings.py.**

### 2. Create a celery.py file root of main project (your_project_app/celery.py)
```
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_app.settings')

app = Celery('your_project_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Configuration for Periodic Tasks for archiving old books in every 30 minutes
app.conf.beat_schedule = {
    'archive-old-books-every-30-minutes': {
        'task': 'your_app.tasks.archive_old_books',
        'schedule': timedelta(minutes=30),
    },
}

```
### Edit __init__.py of your project to load Celery
```
#project_app/__init__.py

from .celery import app as celery_app

__all__ = ('celery_app',)
```
### 4. Django Settings Configuration (settings.py)
```
import os

# Redis as broker
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat settings (for periodic tasks)
INSTALLED_APPS += ['django_celery_beat']
```

### 5. Create the Background Task (your_app/tasks.py)
```
# library/tasks.py

from celery import shared_task
from .models import Book
from datetime import date

@shared_task
def archive_old_books():
    books = Book.objects.filter(published_date__lt=date.today().replace(year=date.today().year - 10))
    books.update(is_archived=True)
    return f"{books.count()} books archived."
```

### 6. Dont forgot to run in individual terminal
- **Terminal 1:**
``` 
celery -A drf_celery_redis_libraryapi worker --loglevel=debug
```
- **Terminal 2:**
``` 
celery -A drf_celery_redis_libraryapi beat --loglevel=debug
```