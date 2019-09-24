"""
data serializers
"""
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from books_api.models import Book, Author

"""
BookSerializer
"""


class BookSerializer(serializers.Serializer):
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField(required=False)
    numberOfPages = serializers.IntegerField()
    publisher = serializers.CharField()
    country = serializers.CharField()
    released = serializers.CharField()


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class BooksModelSerializer(serializers.ModelSerializer):

    authors = AuthorModelSerializer(many=True)

    # authors = serializers.ListField()

    # authors = serializers.StringRelatedField(read_only=False, many=True)
    # authors = PrimaryKeyRelatedField(required=True, many=True,
    #                                      queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'released']

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)

        for author in authors:
            Author.objects.filter(name=author)
            temp_author = Author.objects.create(**author)
            book.authors.add(temp_author)
        return book

    def update(self, instance, validated_data):
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
