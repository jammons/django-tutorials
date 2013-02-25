import datetime
from celery import Celery
from tutorials.books.models import BookLog

celery = Celery('books', broker='django://')


@celery.task
def create_log(user, book):
    # for the record there are better ways to accomplish this. This is for 
    # celery demonstration only.
    now = datetime.datetime.now()
    log = BookLog(time=now, user=user, book=book)
    log.save()
