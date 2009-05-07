import os
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from cms.apps.main.models import Page

# Function for displaying a page.
def page_display(request, page_id, rest_of_url=''):
    # assert False, page_id
    page = get_object_or_404(Page, pk=page_id)
    # assert False, page.template.name
    return render_to_response('site/%s.html' % page.template.name, locals())