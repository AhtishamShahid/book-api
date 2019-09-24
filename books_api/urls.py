"""
# from django.conf.urls import urlrec
"""
from django.urls import path
from . import views

urlpatterns = [
    path('external-books/', views.external_books, name='external-books'),
    path('books/', views.BooksList.as_view(), name='books'),
    path('books/<int:pk>', views.BooksDetail.as_view(), name='books-detail'),
]
