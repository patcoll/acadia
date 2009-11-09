from django.shortcuts import render_to_response
from django.template import RequestContext

def nav_node(node='page'):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                context_dict = output[0]
            elif isinstance(output, dict):
                context_dict = output
            if node in context_dict:
                context_dict['nav_node'] = context_dict[node]
            return output
        return wrapper
    return renderer

def render_page():
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if type(output) != dict or 'page' not in output:
                raise Exception, "Must be a dictionary"
            return render_to_response("pages/%s.html" % \
                       output['page'].template.name, output, \
                       context_instance=RequestContext(request))
            return output
        return wrapper
    return renderer


def render_to(template):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer
