from django.template import Library
from django.conf import settings

register = Library()

def admin_email():
    return settings.ADMIN_EMAIL
admin_email = register.simple_tag(admin_email)

def site_title():
    return settings.SITE_TITLE
site_title = register.simple_tag(site_title)

def cms_title():
    return settings.CMS_TITLE
cms_title = register.simple_tag(cms_title)

