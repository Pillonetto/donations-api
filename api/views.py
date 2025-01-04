from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from . import BookSerializer

# Create a Book (POST request)
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all Books (GET request)
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

# Retrieve a single Book by ID (GET request)
class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_object(pk)
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# Update a Book (PUT request)
class BookUpdate(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def put(self, request, pk):
        book = self.get_object(pk)
        if book:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

# Delete a Book (DELETE request)
class BookDelete(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book:
            book.delete()
            return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
