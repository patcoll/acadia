from django import template
from django.contrib.contenttypes.models import ContentType
import elementtree.ElementTree as et

register = template.Library()

# shortcut to add an html class to an Element (handles multiple classes)
def add_class(obj, c=""):
    if c == "":
        return None
    value = c
    if obj.get("class"):
        value = "%s %s" % (obj.get("class"), value)
    return obj.set("class", value)

class NavigationNode(template.Node):
    # TODO: implement section_nav
    # TODO: implement sitemap
    # TODO: implement two_level
    # TODO: implement yahoo_menu_bar

    def __init__(self, mode, xml="", xml_file=None):
        self.mode = mode
        self.xml = xml
        if xml_file is not None:
            try:
                self.xml = open(xml_file).read()
            except:
                pass
        if self.xml == "":
            raise ValueError, "xml cannot be empty"
        self.tree = et.fromstring(self.xml)
        self.content_type = None
        
    def render(self, context):
        # if not hasattr(self, self.mode):
        #     raise AttributeError, "%r is not a valid navigation mode" % str(self.mode)
        try:
            nav_node = context['nav_node']
        except:
            raise ValueError, "the variable 'nav_node' must exist in the context and be assigned to the object currently being viewed in the navigation"
        
        self.content_type = ContentType.objects.get_for_model(nav_node)
        self.menus = dict((menu.get("name"), menu) for menu in self.tree.getiterator("menu"))
        self.navigation = self.menus['navigation']
        self.parent_map = dict((c, p) for p in self.tree.getiterator() for c in p)
        
        # home page
        self.home_page = self.navigation.find("node")
        
        # hard-code section pages to be the direct sub-elements of the home page.
        self.section_pages = self.home_page.findall("./node")

        self.current_node = None
        self.current_section_node = None
        
        for node in self.navigation.getiterator("node"):
            if int(node.get("contenttype")) == int(self.content_type.id) and int(node.get("objectid")) == int(nav_node.id):
                self.current_node = n = node
                while n.tag == "node":
                    if(self.parent_map[n] == self.home_page):
                        self.current_section_node = n
                    n = self.parent_map[n]
        
        return getattr(self, self.mode, "two_level")()
    
    def breadcrumb(self):
        if self.current_node is None:
            raise ValueError, "Cannot create breadcrumb menu from non-existant current_node"
        
        breadcrumbs = list()
        
        node = self.current_node
        while node.tag == "node":
            breadcrumbs.append(node)
            node = self.parent_map[node]
        breadcrumbs.reverse()
        
        div = et.Element("div", dict(id=self.mode))
        ol = et.SubElement(div, "ol")
        for node in breadcrumbs:
            self._build_links_for(node=node, within=ol)
        return et.tostring(div, encoding="utf-8")
    
    def two_level(self):
        div = et.Element("div", dict(id=self.mode))
        ul = et.SubElement(div, "ul")
        add_class(ul, "main")
        submenus = dict()
        for node in self.section_pages:
            self._build_links_for(node=node, within=ul)
            submenus[node] = list()
            for second_level_node in node.findall("./node"):
                submenus[node].append(second_level_node)
            submenu = et.SubElement(div, "div", dict(id="%s_%s_menu" % (self.mode, node.get("name"))))
            submenu_ul = et.SubElement(submenu, "ul")
            for submenu_node in submenus[node]:
                self._build_links_for(node=submenu_node, within=submenu_ul)
        return et.tostring(div, encoding="utf-8")

    # def sitemap(self):
    #     pass
    
    def _build_links_for(self, node, within):
        li = et.SubElement(within, "li", dict(id="%s_%s" % (self.mode, node.get("name"))))
        a = et.SubElement(li, "a")
        a.text = node.get("title")
        for attr in ("href", "target", "class"):
            if(node.get(attr)):
                a.set(attr, node.get(attr))
        # identify home page
        if(node == self.home_page):
            add_class(li, "homepagelistitem")
            add_class(a, "homepage")
        # identify section page
        if node in self.section_pages:
            add_class(li, "sectionlistitem")
            add_class(a, "section")
        # identify current section node
        if(node == self.current_section_node):
            add_class(li, "currentsectionlistitem")
            add_class(a, "currentsection")
        # identify current node
        if(node == self.current_node):
            add_class(li, "currentpagelistitem")
            add_class(a, "currentpage")


@register.tag(name="navigation")
def do_navigation(parser, token):
    try:
        tag_name, navigation_mode = token.split_contents()
    except ValueError:
        navigation_mode = "sitemap"

    from pages import settings
    return NavigationNode(mode=navigation_mode, xml_file=settings.NAVIGATION_XML)
