from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Fetch all authors and create a new author
class AuthorListView(APIView):
    def get(self, request):    # Fetch all authors
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):   # Create a new author
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetch a single author by ID, update an existing author by ID, and delete an author by ID
class AuthorDetailView(APIView):
    def get(self, request, pk):  # Fetch a single author by ID
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):  # Update an existing author by ID
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Delete an author by ID
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Fetch all books, Fetch book by author name and create a new book
class BookListView(APIView):
    def get(self, request):
        author_name = request.query_params.get('author_name', None)  # Fetch query parameter 'author_name'

        if author_name:
            # Filter books by the author's name (case-insensitive)
            books = Book.objects.filter(author__name__icontains=author_name)
            if not books:
                return Response({"detail": "No books found for this author."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # If no author_name is provided, return all books
            books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):   # Create a new book
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Fetch a single book by ID, update an existing book by ID, and delete a book by ID
class BookDetailView(APIView):
    def get(self, request, pk):  # Fetch a single book by ID
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):  # Update an existing book by ID
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Delete a book by ID
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
