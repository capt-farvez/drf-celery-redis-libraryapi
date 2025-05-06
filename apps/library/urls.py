from django.urls import path
from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

urlpatterns = [
    # Author URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
