from django.conf.urls import patterns, url, include

urlpatterns = patterns('tutorials.books.views',
    url(r'^$', 'index', name='book_index'),
    url(r'^log/$', 'book_log', name='book_logs'),
    url(r'^log_entry/(?P<book_id>\d+)/$', 'mark_read', name='mark_read'),
    url(r'^api/', include('tutorials.books.api.urls')),
)
