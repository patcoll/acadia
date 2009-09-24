"""
>>> from pages.templatetags.navigation import NavigationNode
>>> from pages.models import Page
>>> from django.template.context import Context
>>> from django.core import management
>>> management.call_command('loaddata', 'initial_data.xml', verbosity=0)
>>> NavigationNode()
Traceback (most recent call last):
...
TypeError: __init__() takes at least 2 arguments (1 given)
>>> nn = NavigationNode(mode="breadcrumb", xml='<?xml version="1.0" encoding="utf-8"?><menus><menu title="navigation"><node title="Home Page" name="home" href="/1/home/" contenttype="15" objectid="1"><node title="About Us" name="about-us" href="/2/about-us/" contenttype="15" objectid="2"><node title="Our Mission" name="our-mission" href="/3/our-mission/" contenttype="15" objectid="3" /></node></node></menu></menus>')
>>> c = Context(dict(nav_node=Page.objects.get(title="Our Mission")))
>>> nn.render(c)
'<ol><li class="homepagelistitem" id="breadcrumb_home"><a class="homepage" href="/1/home/">Home Page</a></li><li class="sectionlistitem currentsectionlistitem" id="breadcrumb_about-us"><a class="section currentsection" href="/2/about-us/">About Us</a></li><li class="currentpagelistitem" id="breadcrumb_our-mission"><a class="currentpage" href="/3/our-mission/">Our Mission</a></li></ol>'
>>> c = Context(dict(nav_node=Page.objects.get(title="About Us")))
>>> nn.render(c)
'<ol><li class="homepagelistitem" id="breadcrumb_home"><a class="homepage" href="/1/home/">Home Page</a></li><li class="sectionlistitem currentsectionlistitem currentpagelistitem" id="breadcrumb_about-us"><a class="section currentsection currentpage" href="/2/about-us/">About Us</a></li></ol>'
>>> c = Context(dict(nav_node=Page.objects.get(title="Home Page")))
>>> nn.render(c)
'<ol><li class="homepagelistitem currentpagelistitem" id="breadcrumb_home"><a class="homepage currentpage" href="/1/home/">Home Page</a></li></ol>'
"""