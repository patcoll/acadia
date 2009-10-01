from django import template
from acadia.pages.utils import content_type_slug_for_obj
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

class MenuNode(template.Node):
    def __init__(self, mode, xml="", xml_file=None):
        self.mode = mode
        if self.mode is None:
            self.mode = "two_level"
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
        try:
            nav_node = context['nav_node']
        except:
            raise ValueError, "the variable 'nav_node' must exist in the context and be assigned to the object currently being viewed in the navigation"

        self.content_type = content_type_slug_for_obj(nav_node)
        self.menus = dict((menu.get("name"), menu) for menu in self.tree.getiterator("menu"))
        self.navigation = self.menus['navigation']
        self.parent_map = dict((c, p) for p in self.tree.getiterator() for c in p)
        
        # home page
        self.home_page = self.navigation[0]
        
        # hard-code section pages to be the direct sub-elements of the home page.
        self.section_pages = self.home_page.getchildren()

        self.current_node = None
        self.current_section_node = None
        self.current_path = list()
        
        for node in self.navigation.getiterator("node"):
            if str(node.get("contenttype")) == str(self.content_type) and int(node.get("objectid")) == int(nav_node.id):
                self.current_node = n = node
                while n.tag == "node":
                    self.current_path.append(n)
                    if(self.parent_map[n] == self.home_page):
                        self.current_section_node = n
                    n = self.parent_map[n]

        self.current_path.reverse()

        return getattr(self, self.mode)()

    def breadcrumb(self):
        if self.current_node is None:
            raise ValueError, "Cannot create breadcrumb menu from non-existant current_node"
        div = et.Element("div", dict(id=self.mode))
        ol = et.SubElement(div, "ol")
        if(len(self.current_path) == 1):
            return ""
        for node in self.current_path:
            li = self._build_li_for(node)
            ol.append(li)
        return et.tostring(div, encoding="utf-8")

    def two_level(self):
        div = et.Element("div", dict(id=self.mode))
        ul = et.SubElement(div, "ul")
        add_class(ul, "main")
        submenus = dict()
        for node in self.section_pages:
            li = self._build_li_for(node)
            ul.append(li)
            submenus[node] = list()
            for second_level_node in node.getchildren():
                submenus[node].append(second_level_node)
            submenu = et.SubElement(div, "div", dict(id="%s_%s_menu" % (self.mode, node.get("name"))))
            submenu_ul = et.SubElement(submenu, "ul")
            for submenu_node in submenus[node]:
                submenu_li = self._build_li_for(submenu_node)
                submenu_ul.append(submenu_li)
        if ul.getchildren() == []:
            return ""
        return et.tostring(div, encoding="utf-8")

    def section_nav(self):
        div = et.Element("div", dict(id=self.mode))
        ul = et.SubElement(div, "ul")

        i = 0
        for node in self.current_path[1:]:
            li = self._build_li_for(node)
            if i == 0:
                ul.append(li)
            else:
                for item in ul.getiterator("li"):
                    if item.get("id") == li.get("id"):
                        li = item
            if node.getchildren() == []:
                continue
            ul = et.SubElement(li, "ul")
            for child in node.getchildren():
                child_li = self._build_li_for(child)
                ul.append(child_li)
            i += 1
        if ul.getchildren() == []:
            return ""
        return et.tostring(div, encoding="utf-8")
    
    def sitemap(self):
        div = et.Element("div", dict(id=self.mode))
        ul = et.SubElement(div, "ul")
        
        def process_node(node, within):
            li = self._build_li_for(node)
            within.append(li)
            children = node.getchildren()
            if children != []:
                ul = et.SubElement(li, "ul")
                for child in children:
                    process_node(child, within=ul)
        process_node(self.home_page, within=ul)
        
        return et.tostring(div, encoding="utf-8")
    
    def yahoo_menu_bar(self):
        div = et.Element("div", dict(id=self.mode))
        add_class(div, "yuimenubar yuimenubarnav")
        bd = et.SubElement(div, "div")
        add_class(bd, "bd")
        ul = et.SubElement(bd, "ul")
        for node in self.section_pages:
            li = self._build_li_for(node)
            add_class(li, "yuimenubaritem")
            ul.append(li)
            children = node.getchildren()
            if children != []:
                submenu_div = et.SubElement(li, "div")
                add_class(submenu_div, "yuimenu")
                submenu_bd = et.SubElement(submenu_div, "div")
                add_class(submenu_bd, "bd")
                submenu_ul = et.SubElement(submenu_bd, "ul")
                for child in children:
                    submenu_li = self._build_li_for(child)
                    add_class(submenu_li, "yuimenuitem")
                    submenu_ul.append(submenu_li)
        if ul.getchildren() == []:
            return ""
        return et.tostring(div, encoding="utf-8")

    def _build_li_for(self, node):
        li = et.Element("li", {
            'id': "%s_%s_%s" % (node.get("name"), node.get("contenttype"), node.get("objectid")),
        })
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
        # identify current path
        if node in self.current_path:
            add_class(li, "currentpathlistitem")
            add_class(a, "currentpath")
        # identify current section node
        if(node == self.current_section_node):
            add_class(li, "currentsectionlistitem")
            add_class(a, "currentsection")
        # identify current node
        if(node == self.current_node):
            add_class(li, "currentpagelistitem")
            add_class(a, "currentpage")
        return li

def do_menu(parser, token):
    try:
        tag_name, navigation_mode = token.split_contents()
    except ValueError:
        navigation_mode = None

    from pages import settings
    return MenuNode(mode=navigation_mode, xml_file=settings.NAVIGATION_XML)
register.tag('menu', do_menu)