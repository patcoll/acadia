import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('/opt/local/lib/python2.5/site-packages')

import django.core.handlers.wsgi as wsgi

application = wsgi.WSGIHandler()