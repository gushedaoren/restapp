"""
WSGI config for restapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

path = '/var/restapp/'

if path not in sys.path:

    sys.path.insert(0, path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restapp.settings")

application = get_wsgi_application()
