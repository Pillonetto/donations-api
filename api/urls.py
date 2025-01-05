from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book_list'),
    # path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('redeemed/create/', views.RedeemedStoreItemCreate.as_view(), name='redeemed_create'),
    path('redeemed/', views.RedeemedStoreItemList.as_view(), name='redeemed_list'),
    path('items/', views.StoreItemList.as_view(), name='items_list'),
    path('items/create', views.StoreItemCreate.as_view(), name='items_create'),
]
