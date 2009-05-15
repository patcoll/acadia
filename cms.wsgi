import os, sys
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
application = WSGIHandler()