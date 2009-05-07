import os, sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
application = django.core.handlers.wsgi.WSGIHandler()