import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Paths configuration
CURDIR = os.path.realpath(os.path.dirname(__file__))

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(CURDIR, 'media')
ASSETS_ROOT = os.path.join(MEDIA_ROOT, 'assets')

ADMINS = (
    ('Pat Collins', 'pat@walltowall.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_OPTIONS = {
    # "init_command": "SET storage_engine=INNODB",
}
DATABASE_NAME = 'newcms'       # Or path to database file if using sqlite3.
DATABASE_USER = 'root'       # Not used with sqlite3.
DATABASE_PASSWORD = 'root'     # Not used with sqlite3.
DATABASE_HOST = '127.0.0.1'       # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''       # Set to empty string for default. Not used with sqlite3.

ADMIN_EMAIL = 'pat@walltowall.com'
SITE_TITLE = 'Test Site'
SITE_META_KEYWORDS = ''
SITE_META_DESCRIPTION = ''

GRAPPELLI_ADMIN_TITLE = CMS_TITLE = 'W|W CMS'

# TEMPLATES = {
#     'home': { 'width': 600, 'height': 700 },
#     'section': { 'width': 600, 'height': 700 },
#     'interior': { 'width': 600, 'height': 700 },
# }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Sessions
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# Caching
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

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
MEDIA_URL = '/media/'

ASSET_DIRECTORY = 'assets/'
ASSETS_URL = MEDIA_URL + ASSET_DIRECTORY

# FILEBROWSER_URL_WWW = MEDIA_URL + 'assets/'
# FILEBROWSER_DIRECTORY = "assets/"

# if DEBUG:
#     MEDIA_URL = '/static/media/'
# else:
#     MEDIA_URL = 'http://testdomain.com/static/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'
# TODO: uncomment to enable retrieval of django admin media from a custom directory.
# if DEBUG:
#     ADMIN_MEDIA_PREFIX = 'http://127.0.0.1:8000/media/admin/'
# ADMIN_MEDIA_ROOT = os.path.join(CURDIR, "media", "admin")

# Admin media to load AFTER django admin media
ADMIN_MEDIAMORE_PREFIX = '/media/adminmore/'
ADMIN_MEDIAMORE_ROOT = os.path.join(CURDIR, "media", "adminmore")

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$*G-PG2L^MC*N@^O*$V5AS(0!73UF(FU(B@P!2J@!K7%6CA@&+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    # 'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# to append slash, always have trailing slash in urlconf
APPEND_SLASH = True
ROOT_URLCONF = 'newcms.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    os.path.join(CURDIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    # cms apps
    'newcms.pages',
    'newcms.news',
    # helper apps
    'reversion',
    'south',
    'tagging',
)
