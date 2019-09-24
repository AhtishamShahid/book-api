"""
data serializers
"""

from rest_framework import serializers
from books_api.models import Book, Author


class ApiBookSerializer(serializers.Serializer):
    """
    BookSerializer
    """
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(required=False)
    number_of_pages = serializers.SerializerMethodField('get_number_of_pages')
    publisher = serializers.CharField()
    country = serializers.CharField()
    release_date = serializers.SerializerMethodField('get_release_date')

    def get_release_date(self, instance):
        """
        Over ride default released property
        :param instance:
        :return:
        """
        return instance.released

    def get_number_of_pages(self, instance):
        """
        Over ride default pages property
        :param instance:
        :return:
        """
        return instance.numberOfPages


class AuthorModelSerializer(serializers.ModelSerializer):
    """
    Author Model serializer
    """

    class Meta:
        model = Author
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class BooksModelSerializer(serializers.ModelSerializer):
    """
    Model serializer for books crud
    """
    authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'authors', 'number_of_pages',
                  'publisher', 'country', 'released']

    def create(self, validated_data):
        """
        override create to accommodate creation of relational data
        :param validated_data:
        :return:
        """
        authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)

        for author in authors:
            Author.objects.filter(name=author)
            temp_author = Author.objects.create(**author)
            book.authors.add(temp_author)
        return book

    def update(self, instance, validated_data):
        """
        override create to accommodate creation of relational data
        :param instance:
        :param validated_data:
        :return:
        """
        authors = validated_data.pop('authors')
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.country = validated_data.get('country', instance.country)
        instance.released = validated_data.get('released', instance.released)
        instance.save()

        for author in authors:
            instance.authors.clear()
            temp_author = Author.objects.create(**author)
            instance.authors.add(temp_author)
        return instance
