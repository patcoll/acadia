import os
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *

# shortcut for using RequestContext
def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

# Display a page.
def page_display(request, page_id, rest_of_url=''):
    page = get_object_or_404(Page, pk=page_id)
    nav_node = page
    return render_response(request, "pages/%s.html" % page.template.name, locals())