from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', 'pages.views.pages.display', {'page_id': 1}),
    (r'^(?P<page_id>\d+)/?(?P<rest_of_url>.*)/$', 'pages.views.pages.display'),
)

# custom admin views
# from acadia.admin import admin
# from acadia.pages.views.menus import edit
# 
# admin_urlpatterns = patterns('',
#     url(r'^navigation/$', admin.site.admin_view(edit))
# )

# static media
if settings.DEBUG:
    import os.path
    urlpatterns += patterns('',
        (r'^media/pages/(.*)$', 'django.views.static.serve', dict(document_root=os.path.join(os.path.dirname(__file__), "media", "pages"))),
    )