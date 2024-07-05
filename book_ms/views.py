from rest_framework import viewsets

from book_ms.models import Book
from book_ms.serializer import BookDetailSerializer, BookListSerializer


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):  # using django default modelViewSet for creating default REST API
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookDetailSerializer
