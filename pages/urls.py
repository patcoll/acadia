from django.conf.urls.defaults import *

urlpatterns = patterns('cms.pages.views',
    (r'^$', 'page_display', {'page_id': 1}),
    (r'^(?P<page_id>\d+)/?(?P<rest_of_url>.*)$', 'page_display'),
)
