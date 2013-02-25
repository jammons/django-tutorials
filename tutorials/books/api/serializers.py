from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Book, Author


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author