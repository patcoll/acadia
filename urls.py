from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('pages.urls')),
    (r'^news/', include('news.urls')),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', dict(document_root=settings.MEDIA_ROOT)),
        (r'^assets/(.*)$', 'django.views.static.serve', dict(document_root=settings.ASSETS)),
        (r'^(favicon\.ico|robots\.txt)$', 'django.views.static.serve', dict(document_root=settings.MEDIA_ROOT)),
    )
