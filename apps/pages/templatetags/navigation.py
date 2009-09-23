from django.conf import settings
from django import template

register = template.Library()

@register.tag(name="navigation")
def do_navigation(parser, token):
    try:
        tag_name, navigation_mode = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    navigation_options = ("breadcrumb",)
    if navigation_mode not in navigation_options:
        raise ValueError, "%r is not a valid navigation mode" % str(navigation_mode)

    # shortcut to add an html class to an Element (handles multiple classes)
    def add_class(obj, c=""):
        if c == "":
            return None
        value = c
        if obj.get("class"):
            value = "%s %s" % (obj.get("class"), value)
        obj.set("class", value)
    
    class NavigationNode(template.Node):
        def __init__(self, mode):
            self.mode = mode
        def render(self, context):
            try:
                nav_node = context['nav_node']
            except:
                raise ValueError, "the variable 'nav_node' must exist in the context and be assigned to the object currently being viewed in the navigation"

            from django.contrib.contenttypes.models import ContentType
            content_type = ContentType.objects.get_for_model(nav_node)
            
            import elementtree.ElementTree as et
            tree = et.parse(settings.NAVIGATION_XML)
            
            menus = dict((menu.get("title"), menu) for menu in tree.getiterator("menu"))
            
            navigation = menus['navigation']
            
            # home page
            home_page = navigation.find("node")
            add_class(home_page, "homepage")
            
            # hard-code section pages to be the direct sub-elements of the home page.
            section_pages = home_page.findall("./node")
            for section_page in section_pages:
                add_class(section_page, "sectionpage")

            # find current node
            current_node = None
            for node in navigation.getiterator("node"):
                if int(node.get("contenttype")) == int(content_type.id) and int(node.get("objectid")) == int(nav_node.id):
                    current_node = node

            if self.mode == "breadcrumb":
                if current_node is None:
                    raise ValueError, "Cannot create breadcrumb menu from non-existant current_node"
                
                breadcrumbs = list()
                parent_map = dict((c, p) for p in tree.getiterator() for c in p)
                
                node = current_node
                while node.tag == "node":
                    breadcrumbs.append(node)
                    node = parent_map[node]
                breadcrumbs.reverse()
                
                ol = et.Element("ol")
                for node in breadcrumbs:
                    li = et.SubElement(ol, "li", dict(id="%s_%s" % (self.mode, node.get("name"))))
                    a = et.SubElement(li, "a")
                    a.text = node.get("title")
                    for attr in ("href", "target", "class"):
                        if(node.get(attr)):
                            a.set(attr, node.get(attr))
                    # identify current node with some classes
                    if(node == current_node):
                        add_class(li, "currentpagelistitem")
                        add_class(a, "currentpage")
                return et.tostring(ol)
            # nothing to return
            return None
    return NavigationNode(navigation_mode)