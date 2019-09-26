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
    books_url = reverse('books')

    data = {
        "name": "My Book",
        "isbn": "axm4ss",
        "number_of_pages": 100,
        "publisher": "Republic Publisher",
        "country": "Pakistan",
        "released": "2010-10-10",
        "authors": []

    }

    def test_create_book(self):
        """
        Ensure we can create a new book and .
        """

        response = self.client.post(self.books_url, data=self.data, format='json')
        response_data = response.data['data']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['name'], self.data['name'])
        self.assertEqual(response_data['isbn'], self.data['isbn'])
        self.assertEqual(response_data['number_of_pages'], self.data['number_of_pages'])
        self.assertEqual(response_data['publisher'], self.data['publisher'])
        self.assertEqual(response_data['country'], 'PK')
        self.assertEqual(response_data['released'], self.data['released'])
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(Book.objects.count(), 1)

    def test_update_book(self):
        """
        Ensure we can delete a new book .
        """

        record = self.client.post(reverse('books'), data=self.data, format='json')

        self.data['name'] = 'My book 2'
        path = self.books_url + str(record.data['data']['id'])
        response = self.client.put(path, data=self.data, format='json')
        response_data = response.data['data']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['name'], self.data['name'])
        self.assertEqual(response_data['isbn'], self.data['isbn'])
        self.assertEqual(response_data['number_of_pages'], self.data['number_of_pages'])
        self.assertEqual(response_data['publisher'], self.data['publisher'])
        self.assertEqual(response_data['country'], 'PK')
        self.assertEqual(response_data['released'], self.data['released'])
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(Book.objects.count(), 1)

    def test_list_book(self):
        """
        Ensure we can list a new book .
        """

        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], [])
        self.assertEqual(response.data['status'], 'success')

    def test_delete_book(self):
        """
        Ensure we can delete a new book .
        """
        record = self.client.post(self.books_url, data=self.data, format='json')
        response = self.client.delete(self.books_url + str(record.data['data']['id']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['data'], [])
        self.assertEqual(response.data['status'], 'success')


class BooksAPITest(APITestCase):
    def test_api_ice_and_fire_response(self):
        """
        Test Data in books received from api
        :return:
        """
        response = self.client.get(reverse('external-books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
