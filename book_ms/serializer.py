from rest_framework import serializers

from book_ms.models import Book


class BookListSerializer(serializers.ModelSerializer):  # Writing serializer for list display of book
    class Meta:
        model = Book
        fields = ("id", "title", "author", "published_date")


class BookDetailSerializer(serializers.ModelSerializer):  # Writing serializer for detail book display and using it for formm
    class Meta:
        model = Book
        fields = "__all__"
