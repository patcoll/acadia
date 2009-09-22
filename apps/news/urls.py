from django.conf.urls.defaults import *
from django.conf import settings
from views import *

urlpatterns = patterns('',
  (r'^$', post_index),
  (r'^(\d+)$', post_view),
  (r'^categories/$', category_index),
  (r'^categories/(\d+)$', category_view),
)