from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='books')
    readers = models.ManyToManyField(User, related_name='read_books',
        editable=False, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.title


class BookLog(models.Model):
    ''' Keeps track of when a user reads a book '''
    time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='logs')
    book = models.ForeignKey(Book, related_name='logs')

    def __unicode__(self):
        return '{}: {}'.format(self.user, self.book)

