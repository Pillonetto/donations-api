from rest_framework import serializers
from .models import Book, StoreItem, RedeemedStoreItem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = '__all__'

class RedeemedStoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeemedStoreItem
        fields = '__all__'