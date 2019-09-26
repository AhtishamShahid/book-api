"""
data serializers
"""
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from books_api.models import Book, Author, Publisher
from django_countries.serializer_fields import CountryField


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
        return instance['released']

    def get_number_of_pages(self, instance):
        """
        Over ride default pages property
        :param instance:
        :return:
        """
        return instance['numberOfPages']


class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class BooksModelSerializer(serializers.ModelSerializer):
    """
    Model serializer for books crud
    """
    authors = CreatableSlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Author.objects.all()
    )
    country = CountryField()

    publisher = CreatableSlugRelatedField(
        slug_field='name',
        queryset=Publisher.objects.all()
    )

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'authors', 'number_of_pages',
                  'publisher', 'country', 'released']
