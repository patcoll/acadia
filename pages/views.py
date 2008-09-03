from django.shortcuts import render_to_response, get_object_or_404
from cms.pages.models import *

# Function for displaying a page.
def page_display(request, page_id, rest_of_url=''):
    assert False, rest_of_url
    page = get_object_or_404(Page, pk=page_id)
    # return render_to_response('')
    # pass