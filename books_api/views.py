"""
# Create your views here.
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import anapioficeandfire

from books_api.models import Book
from books_api.serializers import ApiBookSerializer, BooksModelSerializer


@api_view(['GET'])
def external_books(request):
    """
    Query and get books data form ice and fire api
    :param request:
    :return:
    """
    api = anapioficeandfire.API()
    instance = api.get_books(name=request.GET.get('name'))
    serializer = ApiBookSerializer(instance, many=True)
    return Response(status=200, data={
        "status_code": status.HTTP_200_OK,
        "status": "success",
        'data': serializer.data,
    })


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):  # pylint:disable=too-many-ancestors
    """
    CBV for Recipe detail page
    """
    queryset = Book.objects.all()
    serializer_class = BooksModelSerializer

    def delete(self, request, *args, **kwargs):
        data = self.get_object()
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT, data={
            "status_code": status.HTTP_204_NO_CONTENT,
            "status": "success",
            "message": "The " + data.name + "  was deleted successfully",
            "data": []
        })

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        data = self.get_object()
        return Response(status=status.HTTP_200_OK, data={
            "status_code": 200,
            "status": "success",
            "message": "The " + data.name + " was updated successfully",
        })

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            'data': serializer.data,
            "status_code": 200,
            "status": "success",
        }
        return Response(status=status.HTTP_200_OK, data=data)


class BooksList(generics.ListCreateAPIView):
    """
    Recipe listing view
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'country', 'publisher', 'released']
    queryset = Book.objects.all()
    serializer_class = BooksModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = {
            'data': serializer.data,
            "status_code": 200,
            "status": "success",
        }
        return Response(status=status.HTTP_200_OK, data=data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': serializer.data,
            "status_code": status.HTTP_201_CREATED,
            "status": "success",
        }
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
