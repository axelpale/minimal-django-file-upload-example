# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
	(r'^myapp/', include('myproject.myapp.urls')),
	(r'^$', redirect_to, {'url': '/myapp/list/'}), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
