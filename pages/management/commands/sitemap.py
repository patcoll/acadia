from django.core.management.base import BaseCommand
from optparse import make_option
from pages import settings
from pages.models import Page
import os
import sys
import yaml

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-f', '--file', dest='sitemap_file', default=settings.SITEMAP_FILE,
            help='The file path of the sitemap file to parse.'),
    )
    help = """Loads a sitemap YAML file with this kind of syntax:

Home:
  About Us:
    - Our Mission
"""
    # args = '[appname ...]'

    # requires_model_validation = False

    def handle(self, *args, **options):
        sitemap_file = options.get("sitemap_file", settings.SITEMAP_FILE)
        if not os.path.exists(sitemap_file):
            sys.exit("File not found:\n  %s" % sitemap_file)
        print("Importing the sitemap will delete all existing Page objects.\nAre you sure? [y/N]")
        
        read = sys.stdin.readline()
        if read.strip().lower() != 'y':
            sys.exit(1)
        
        
        contents = open(sitemap_file).read()
        # print(contents)
        # print(yaml)
        # import elementtree.ElementTree as et
        
        Page.objects.all().delete()
        data = yaml.load(contents)
        
        menu_names = data.keys() # dict((title, menu) for title, menu in data.items())
        # print(menu_names)
        
        # print()
        # for title, menu in data.items():
        #     print(k)
        #     print(v)
        
        # print()
        # from django.conf import settings
        # from django.test.utils import get_runner

        # verbosity = int(options.get('verbosity', 1))
        # interactive = options.get('interactive', True)
        # test_runner = get_runner(settings)

        # failures = test_runner(test_labels, verbosity=verbosity, interactive=interactive)
        # if failures:
        #     sys.exit(failures)
