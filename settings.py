import os, sys

DEPLOYED = False

DEBUG = not(DEPLOYED)
TEMPLATE_DEBUG = DEBUG

# Paths configuration
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FRONT_END = os.path.join(ROOT_DIR, 'frontend')
ASSETS = os.path.join(FRONT_END, 'assets')
# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(FRONT_END, 'media')

# add 'vendor' dir to PYTHONPATH
sys.path.append('/opt/local/lib/python2.5/site-packages')
sys.path.append(os.path.join(ROOT_DIR, 'vendor'))


ADMINS = (
    ('Pat Collins', 'pat@burned.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_OPTIONS = {"init_command": "SET storage_engine=INNODB"}
DATABASE_NAME = 'django_cms'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'root'         # Not used with sqlite3.
DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if DEPLOYED:
    MEDIA_URL = 'http://burned.com/media/'
else:
    MEDIA_URL = 'http://localhost:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+&@ac6%7k!@j2!p@b(uf(fu37!0(sa5v$*o^@n*cm^l2gp-g*$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'cms.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    os.path.join(FRONT_END, 'templates'),
    os.path.join(ROOT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'MySQLdb',
    'cms.main',
    'django_evolution',
    'mptt',
    'tagging',
    'yaml',
)
