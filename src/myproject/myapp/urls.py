from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('myapp.views',
    url(r'^list/$', 'list', name='list'),
)
