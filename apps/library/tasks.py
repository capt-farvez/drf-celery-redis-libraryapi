from celery import shared_task
from datetime import date
from .models import Book

@shared_task
def archive_old_books():
    ten_years_ago = date.today().replace(year=date.today().year - 10)
    # print(f"Archiving books published before {ten_years_ago}...")
    books_to_archive = Book.objects.filter(is_archived=False, published_date__lt=ten_years_ago)
    # print(f"Books to archive: {books_to_archive.count()}")
    books_to_archive.update(is_archived=True)
    return f"Archived {books_to_archive.count()} - {ten_years_ago} books."

