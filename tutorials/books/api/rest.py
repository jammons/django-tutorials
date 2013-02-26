from rest_framework import generics

from .serializers import BookSerializer, AuthorSerializer
from ..models import Book, Author


class BookList(generics.ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer


class AuthorList(generics.ListCreateAPIView):
    model = Author
    serializer_class = AuthorSerializer

