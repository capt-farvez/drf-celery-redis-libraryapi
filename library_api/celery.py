import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_api.settings')

app = Celery('library_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.worker_pool = 'solo'

app.autodiscover_tasks()

# Celery Beat Configuration for Periodic Tasks for archiving old books in every 30 minutes
app.conf.beat_schedule = {
    'archive-old-books-every-30-minutes': {
        'task': 'apps.library.tasks.archive_old_books',
        'schedule': timedelta(minutes=30),
    },
}
