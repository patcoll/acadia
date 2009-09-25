from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from optparse import make_option
from pages import settings
from django.contrib.contenttypes.models import ContentType
from pages.models import Page, User
import os
import sys
import yaml
import elementtree.ElementTree as et

def underscore(words):
    import re
    underscored = str(words)
    subs = [
        (r'[^A-Za-z0-9_-]', r'_'),
        (r'([A-Z]+)([A-Z][a-z])', r'\1_\2'),
        (r'([a-z\d])([A-Z])', r'\1_\2'),
        (r'-', r'_')
    ]
    for pattern, replacement in subs:
        underscored = re.sub(pattern, replacement, underscored)
    underscored = underscored.lower()
    return underscored

def slugify(words):
    import re
    slug = str(words.strip().lower())
    subs = [
        (r'[^A-Za-z0-9_-]', r'_'),
        (r'_', r'-'),
    ]
    for pattern, replacement in subs:
        slug = re.sub(pattern, replacement, slug)
    return slug

def camelize(underscored_word):
    pass

class MyLoader(yaml.Loader):
    """Custom YAML loader.

    Overrides `construct_mapping` with `construct_pairs`,
    which essentially constructs the Python data structure
    with lists of tuples instead of dictionaries, which
    allows us to retain the order in which the YAML was
    originally written. Otherwise nodes on each level would
    be alphabetized. Technique taken from PyYAML unit tests.

    Note: Uncomment the sort() line if you still want each
    level sorted.

    @see http://pyyaml.org/ticket/29
    @see http://pyyaml.org/browser/pyyaml/trunk/tests/lib/test_structure.py?rev=330#L137
    """
    def construct_sequence(self, node):
        return tuple(yaml.Loader.construct_sequence(self, node))
    def construct_mapping(self, node):
        pairs = self.construct_pairs(node)
        # pairs.sort()
        return pairs
    def construct_undefined(self, node):
        return self.construct_scalar(node)


MyLoader.add_constructor(u'tag:yaml.org,2002:map', MyLoader.construct_mapping)
MyLoader.add_constructor(None, MyLoader.construct_undefined)


# def camelize(lower_case_and_underscored_word, first_letter_in_uppercase = true)
#   if first_letter_in_uppercase
#     lower_case_and_underscored_word.to_s.gsub(/\/(.?)/) { "::" + $1.upcase }.gsub(/(^|_)(.)/) { $2.upcase }
#   else
#     lower_case_and_underscored_word.first + camelize(lower_case_and_underscored_word)[1..-1]
#   end
# end


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-f', '--file', dest='sitemap_file', default=settings.SITEMAP_FILE,
            help='The file path of the sitemap file to parse.'),
    )
    help = """Loads a sitemap YAML file with this kind of syntax:

Navigation:
  Home:
    Vestibulum Leo:
      Fermentum Viverra:
        Aliquam Interdum:
        Phasellus at Nisl:
        Duis Faucibus:
        Ornare Ultrices Turpis:
      Mauris:
        Sodales Vel Viverra:
        Elementum:
        Lectus Felis Vel:
Not In Navigation:
  Faucibus Sodales Ornare:
    Sodales:
    Curabitur Tempor Lobortis:
      Donec Fermentum:
    Dolor Bibendum:
    Consectetur Tellus:
    Pellentesque:
"""
    # args = '[appname ...]'

    def __init__(self):
        BaseCommand.__init__(self)
        self.style = no_style()
        self.content_type = ContentType.objects.get_for_model(Page)
        self.default_user = User.objects.get(id=1)

    def _parse_sitemap(self, list_node, menu_node):
        """Recursively parse sitemap parsed from a YAML file.

        Will populate the ElementTree node in `menu_node` and will do so
        in a recursive manner.

        @list_node The portion of the list we are parsing
        @menu_node The ElementTree node where we'll append nodes
        """
        for title, children in list_node:
            n = et.SubElement(menu_node, "node")
            p = Page(title=title, name=slugify(title), user=self.default_user)
            p.save()
            xml_attr = dict(title=p.title, name=p.name, href=p.get_absolute_url(), contenttype=str(self.content_type.id), objectid=str(p.id))
            for key, value in xml_attr.items():
                n.set(key, value)
            if children is not None:
                self._parse_sitemap(children, n)

    def parse_sitemap(self, yaml_text):
        """Parse YAML and return a valid ElementTree.
        """
        # delete all pages
        from django.db import connection, transaction
        cursor = connection.cursor()

        # generate "flush" sql queries from db backend for the pages table.
        # for mysql this will be a "truncate" query plus an "auto_increment" reset query.
        for query in connection.ops.sql_flush(self.style, [Page._meta.db_table], [dict(table=Page._meta.db_table)]):
            cursor.execute(query)
        transaction.commit_unless_managed()

        # load with our custom loader
        data = yaml.load(yaml_text, Loader=MyLoader)

        # tally up pages and build a new ElementTree at the same time.
        root = et.Element("menus")

        for menu_name, menu in data:
            menu_node = et.SubElement(root, "menu")
            menu_node.set("title", menu_name)
            menu_node.set("name", underscore(menu_name))
            self._parse_sitemap(menu, menu_node)

        return et.ElementTree(root)

    def handle(self, *args, **options):
        sitemap_file = options.get("sitemap_file", settings.SITEMAP_FILE)
        if not os.path.exists(sitemap_file):
            sys.exit("File not found:\n  %s" % sitemap_file)
        print("Importing the sitemap will delete all existing Page objects.\nAre you sure? [y/N]")

        read = sys.stdin.readline()
        if read.strip().lower() != 'y':
            sys.exit(1)

        tree = self.parse_sitemap(open(sitemap_file).read())

        # write new navigation xml
        tree.write(settings.NAVIGATION_XML, encoding="utf-8")

