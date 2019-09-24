"""
# from django.conf.urls import urlrec
"""
from django.urls import path
from . import views

urlpatterns = [
    path('external-books/', views.external_books, name='external-books'),
    path('v1/books/', views.BooksList.as_view(), name='books'),
    path('v1/books/<int:pk>', views.BooksDetail.as_view(), name='books-detail'),
]
