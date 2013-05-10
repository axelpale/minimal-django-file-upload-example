# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
)
