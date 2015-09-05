import os
import sys

sys.path.append('/var/restapp/')
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'restapp.settings'
application = get_wsgi_application()
