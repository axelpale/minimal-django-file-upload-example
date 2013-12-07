minimal-django-file-upload-example
==================================

Project contains source code that was made originally for the [Django file upload example at StackOverflow](http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example).

The goal with minimal-django-file-upload-example is to demonstrate and teach how file uploading is done with Django. Because of the academic nature of the project all the extra functionality is left out. Otherwise you would have hard time to quess what is important and what is not.

Currently [Django 1.3](https://docs.djangoproject.com/en/dev/releases/1.3/), [Django 1.4](https://docs.djangoproject.com/en/dev/releases/1.4/), [Django 1.5](https://docs.djangoproject.com/en/dev/releases/1.5/) and [Django 1.6](https://docs.djangoproject.com/en/dev/releases/1.6/) are supported. See [src/for_django_1-x/](https://github.com/doph/minimal-django-file-upload-example/tree/master/src) for the corresponding code.

Differences between code for Django 1.3 and 1.4
-----------------------------------------------
- Directory hierachy follows Django's defaults. For example manage.py has risen one level up.
- Due to hierarchy change absolute package paths are now more recommended and therefore used. Look INSTALLED_APPS in settings.py for example.
- Little more comments
- More encoding definitions # -*- coding: utf-8 -*-
- Database renamed to database.sqlite3

Differences between code for Django 1.4 and 1.5
-----------------------------------------------
- urls.py: Django 1.5 recommends RedirectView to be used instead of django.views.generic.simple.redirect_to. See [RedirectView](https://docs.djangoproject.com/en/1.5/ref/class-based-views/base/#redirectview) for details.
- list.html: url template tag requires view names to be double quoted. See [Django 1.5 release note overview](https://docs.djangoproject.com/en/dev/releases/1.5/#overview) for details.

Differences between code for Django 1.5 and 1.6
-----------------------------------------------
- myapp/urls.py: changed `from django.conf.urls import patterns, url` to `from django.conf.urls.defaults import patterns, url`
