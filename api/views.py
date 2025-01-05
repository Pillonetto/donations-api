from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, StoreItem, RedeemedStoreItem
from .serializers import BookSerializer, StoreItemSerializer, RedeemedStoreItemSerializer

# Create a Book (POST request)
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create a Book (POST request)
class StoreItemCreate(APIView):
    def post(self, request):
        serializer = StoreItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedeemedStoreItemCreate(APIView):
    def post(self, request):
        serializer = RedeemedStoreItemSerializer(data=request.data)
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

# List all Items (GET request)
class StoreItemList(APIView):
    def get(self, request):
        storeItems = StoreItem.objects.all()
        serializer = StoreItemSerializer(storeItems, many=True)
        return Response(serializer.data)

# List all Items (GET request)
class RedeemedStoreItemList(APIView):
    def get(self, request):
        storeItems = RedeemedStoreItem.objects.all()
        serializer = RedeemedStoreItemSerializer(storeItems, many=True)
        return Response(serializer.data)

