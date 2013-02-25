from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', base_views.redirect_to_index),
    url(r'^books/', include('tutorials.books.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
