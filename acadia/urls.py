from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from acadia.admin import CustomAdminSite
admin.site = CustomAdminSite()
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
        # TODO: uncomment to enable retrieval of django admin media from a custom directory.
        # (r'^media/admin/(.*)$', 'django.views.static.serve', dict(document_root=settings.ADMIN_MEDIA_ROOT)),
        # Admin media to load AFTER django admin media
        (r'^media/adminmore/(.*)$', 'django.views.static.serve', dict(document_root=settings.ADMIN_MEDIAMORE_ROOT)),
        (r'^media/(.*)$', 'django.views.static.serve', dict(document_root=settings.MEDIA_ROOT)),
        (r'^assets/(.*)$', 'django.views.static.serve', dict(document_root=settings.ASSETS_ROOT)),
        (r'^(favicon\.ico|robots\.txt)$', 'django.views.static.serve', dict(document_root=settings.MEDIA_ROOT)),
    )
