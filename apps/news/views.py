import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

# Function for displaying a page.
def post_index(request):
    return HttpResponse('posts')
  
def post_view(request, post_id):
    return HttpResponse('post: %s' % post_id)
  
def category_index(request):
    return HttpResponse('categories')

def category_view(request, category_id):
    return HttpResponse('category: %s' % category_id)
