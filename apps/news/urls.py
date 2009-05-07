from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('cms.apps.news.views',
  (r'^$', 'post_index'),
  (r'^(\d+)$', 'post_view'),
  (r'^categories/$', 'category_index'),
  (r'^categories/(\d+)$', 'category_view'),
)