"""
# Create your views here.
"""
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view

from books_api.ice_and_fire_api import IceAndFireAPI
from books_api.messages import UPDATE_MESSAGE, DELETE_MESSAGE
from books_api.models import Book, Publisher
from books_api.serializers import ApiBookSerializer, BooksModelSerializer
from books_api.util import make_response


@api_view(['GET'])
def external_books(request):
    """
    Query and get books data form ice and fire api
    :param request:
    :return:Response
    """
    response = IceAndFireAPI().get_books(query=request.GET)
    response.data = ApiBookSerializer(response.data, many=True).data
    return make_response(response)


class BooksList(generics.ListCreateAPIView):
    """
    Books listing view
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'country', 'released']

    queryset = Book.objects.all()
    serializer_class = BooksModelSerializer

    def get_queryset(self):
        publisher_query = self.request.GET.get('publisher')
        if publisher_query is not None:
            try:
                publisher = Publisher.objects.filter(name=self.request.GET.get('publisher'))[0]
                return self.queryset.filter(publisher=publisher)
            except:
                return self.queryset
        else:
            return self.queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return make_response(response)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return make_response(response)


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Book  detail view
    """
    queryset = Book.objects.all()
    serializer_class = BooksModelSerializer

    def delete(self, request, *args, **kwargs):
        message = DELETE_MESSAGE.format(self.get_object().name)
        response = self.destroy(request, *args, **kwargs)
        return make_response(response, message)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        message = UPDATE_MESSAGE.format(self.get_object().name)
        return make_response(response, message)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return make_response(response)
