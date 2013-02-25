from django.conf.urls import patterns, url

from .rest import BookList, AuthorList

urlpatterns = patterns('',
    url(
        r'^books/$',
        BookList.as_view(),
        name='books_api'
    ),
    url(
        r'^authors/$',
        AuthorList.as_view(),
        name='authors_api'
    ),
)
