from django.shortcuts import get_object_or_404
# from acadia.pages.views.shortcuts import render_response
from acadia.pages.models import Page
from acadia.pages.views.decorators import nav_node, render_page

def display(request, page_id, rest_of_url=''):
    page = get_object_or_404(Page, pk=page_id)
    return locals()
display = nav_node('page')(display)
display = render_page()(display)