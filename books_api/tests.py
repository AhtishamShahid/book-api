from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books_api.models import Book
from books_api.views import BooksList


class BooksTest(APITestCase):
    """
    Test Recipe CRUD
    """

    def setUp(self):
        """
         # We want to go ahead and originally create a RecipeTest.
        :return:
        """

        self.create_url = reverse('books')

    def test_create_book(self):
        """
        Ensure we can create a new book and .
        """
        data = {
            "name": "My Book",
            "isbn": "axm4ss",
            "number_of_pages": 100,
            "publisher": "Republic Publisher",
            "country": "Pakistan",
            "released": "2010-10-10",
            "authors": []

        }
        response = self.client.post(reverse('books'), data=data, format='json')
        response_data = response.data['data']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['name'], data['name'])
        self.assertEqual(response_data['isbn'], data['isbn'])
        self.assertEqual(response_data['number_of_pages'], data['number_of_pages'])
        self.assertEqual(response_data['publisher'], data['publisher'])
        self.assertEqual(response_data['country'], data['country'])
        self.assertEqual(response_data['released'], data['released'])
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(Book.objects.count(), 1)

    def test_list_book(self):
        """
        Ensure we can list a new book .
        """

        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], [])
        self.assertEqual(response.data['status'], 'success')

    def test_delete_book(self):
        """
        Ensure we can delete a new book .
        """
        data = {
            "name": "My Book",
            "isbn": "axm4ss",
            "number_of_pages": 100,
            "publisher": "Republic Publisher",
            "country": "Pakistan",
            "released": "2010-10-10",
            "authors": []

        }
        record = self.client.post(reverse('books'), data=data, format='json')
        response = self.client.delete(reverse('books') + str(record.data['data']['id']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['data'], [])
        self.assertEqual(response.data['status'], 'success')
