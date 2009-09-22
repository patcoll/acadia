from os import environ
environ['DJANGO_SETTINGS_MODULE'] = 'newcms.settings'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()