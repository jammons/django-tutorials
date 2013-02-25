from django.contrib import admin
from tutorials.books.models import Book, Author, BookLog

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookLog)
