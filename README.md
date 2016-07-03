minimal-django-file-upload-example
==================================

Project contains source code that was made originally for the [Django file upload example at StackOverflow](http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example).

The goal with minimal-django-file-upload-example is to demonstrate and teach how file uploading is done with Django. Because of the academic nature of the project all the extra functionality is left out. Otherwise you would have hard time to guess what is important and what is not.

The following Django versions are supported:  
- [Django 1.9](https://docs.djangoproject.com/en/dev/releases/1.9/) | [source](../../tree/master/src/for_django_1-9/myproject).
- [Django 1.8](https://docs.djangoproject.com/en/dev/releases/1.8/) | [source](../../tree/master/src/for_django_1-8/myproject).
- [Django 1.7](https://docs.djangoproject.com/en/dev/releases/1.7/) | [source](../../tree/master/src/for_django_1-7/myproject).
- [Django 1.6](https://docs.djangoproject.com/en/dev/releases/1.6/) | [source](../../tree/master/src/for_django_1-6/myproject).
- [Django 1.5](https://docs.djangoproject.com/en/dev/releases/1.5/) | [source](../../tree/master/src/for_django_1-5/myproject).
- [Django 1.4](https://docs.djangoproject.com/en/dev/releases/1.4/) | [source](../../tree/master/src/for_django_1-4/myproject).
- [Django 1.3](https://docs.djangoproject.com/en/dev/releases/1.3/) | [source](../../tree/master/src/for_django_1-3/myproject).

Usage (Django 1.9)
------------------
First ensure you have Django 1.9 installed. Then:

    $ git clone https://github.com/axelpale/minimal-django-file-upload-example.git
	$ cd minimal-django-file-upload-example
	$ cd src/for_django_1-9/myproject
	$ python manage.py migrate
	$ python manage.py runserver


Differences between code for Django 1.7 and 1.8
-----------------------------------------------
- settings.py: New TEMPLATE settings. See [upgrading instructions](https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/) for details.
- settings.py: reverted to the default directory for db.sqlite3 database and  media dir.
- urls.py: Added explicit RedirectView permanent argument: `RedirectView.as_view(url='/myapp/list/', permanent=True))`


Differences between code for Django 1.6 and 1.7
-----------------------------------------------
- use `./manage.py migrate` instead of `./manage.py syncdb`


Differences between code for Django 1.5 and 1.6
-----------------------------------------------
- myapp/urls.py: changed the line `from django.conf.urls.defaults import patterns, url` to `from django.conf.urls import patterns, url`


Differences between code for Django 1.4 and 1.5
-----------------------------------------------
- urls.py: Django 1.5 recommends RedirectView to be used instead of django.views.generic.simple.redirect_to. See [RedirectView](https://docs.djangoproject.com/en/1.5/ref/class-based-views/base/#redirectview) for details.
- list.html: url template tag requires view names to be double quoted. See [Django 1.5 release note overview](https://docs.djangoproject.com/en/dev/releases/1.5/#overview) for details.


Differences between code for Django 1.3 and 1.4
-----------------------------------------------
- Directory hierachy follows Django's defaults. For example manage.py has risen one level up.
- Due to hierarchy change absolute package paths are now more recommended and therefore used. Look INSTALLED_APPS in settings.py for example.
- Little more comments
- More encoding definitions # -*- coding: utf-8 -*-
- Database renamed to database.sqlite3
