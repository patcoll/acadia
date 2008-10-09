import os
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from cms.main.models import *

# Function for displaying a page.
def page_display(request, page_id, rest_of_url=''):
    print page_id
    page = get_object_or_404(Page, pk=page_id)
    return render_to_response(os.path.join(settings.FRONT_END, 'templates', 'interior.html'), locals())