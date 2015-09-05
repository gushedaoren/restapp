import os
import sys

sys.path.append('/var/restapp/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'restapp.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()