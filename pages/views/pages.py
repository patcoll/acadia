from django.shortcuts import get_object_or_404
from newcms.pages.views.shortcuts import render_response
from newcms.pages.models import Page

def display(request, page_id, rest_of_url=''):
    page = get_object_or_404(Page, pk=page_id)
    nav_node = page
    return render_response(request, "pages/%s.html" % page.template.name, locals())