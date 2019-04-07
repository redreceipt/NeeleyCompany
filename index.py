"""
WSGI config for neeley_company project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neeley_company.settings")

app = get_wsgi_application()
os.system("python manage.py migrate")
os.system("python manage.py runserver")
