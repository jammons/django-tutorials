from django.http import HttpResponse
from django.shortcuts import render
from tutorials.books.models import Book, BookLog
from tutorials.books.tasks import create_log

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

def book_log(request):
    logs = BookLog.objects.all()
    return render(request, 'books/book_log.html', { 'logs': logs })

def mark_read(request, book_id=None):
    if book_id:
        book = Book.objects.get(id=book_id)
        create_log.delay(request.user, book) 
        return HttpResponse('Sent off for Processing')
    else:
        return HttpResponse('No ID match')
        
