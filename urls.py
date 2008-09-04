from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('cms.main.urls')),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

if not settings.DEPLOYED:
    import os
    urlpatterns += patterns('',
        # Resources (for testing)
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )