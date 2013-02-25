from django.conf.urls import patterns, include, url
from django.contrib import admin
import views as base_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', base_views.redirect_to_index),
    url(r'^books/', include('tutorials.books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
