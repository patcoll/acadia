from django.conf.urls.defaults import *
from django.conf import settings
from views import page_display

urlpatterns = patterns('',
    (r'^$', page_display, {'page_id': 1}),
    (r'^(?P<page_id>\d+)/?(?P<rest_of_url>.*)/$', page_display),
)

if settings.DEBUG:
    import os.path
    urlpatterns += patterns('',
        (r'^pages/media/(.*)$', 'django.views.static.serve', dict(document_root=os.path.join(os.path.dirname(__file__), "media", "pages"))),
    )