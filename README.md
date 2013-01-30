minimal-django-file-upload-example
==================================

Project contains source code that was made originally for the Django file upload example at http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example

The goal with minimal-django-file-upload-example is to demonstrate and teach how the file uploading is done with Django. Because of the academic nature of the project all the extra functionality is left out. Otherwise you would have hard time to quess what is important and what is not.

Currently the code is available for Django 1.3 and Django 1.4. See src/for_django_1-3/ and src/for_django_1-4/

Differences between implementations for django 1.3 and 1.4
----------------------------------------------------------
- Directory hierachy follows Django's defaults. For example manage.py has risen one level up.
- Due to hierarchy change absolute package paths are now more recommended and therefore used. Look INSTALLED_APPS in settings.py for example.
- Little more comments
- More encoding definitions # -*- coding: utf-8 -*-
- Database renamed to database.sqlite3
