from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('cms.main.views',
  (r'^$', 'page_display', {'page_id': 1}),
  (r'^(?P<page_id>\d+)/?(?P<rest_of_url>.*)$', 'page_display'),
)

if not settings.DEPLOYED:
  import os
  urlpatterns += patterns('',
    # Resources (for testing)
    # (r'^static/media/(.*)$', 'django.views.static.serve', {
    #   'document_root': settings.MEDIA_ROOT
    # }),
    # (r'^static/assets/(.*)$', 'django.views.static.serve', {
    #   'document_root': settings.ASSETS
    # }),
  )