from django.template import Library

register = Library()

def admin_mediamore_prefix():
    """
    Returns the string contained in the setting ADMIN_MEDIA_PREFIX.
    """
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return settings.ADMIN_MEDIAMORE_PREFIX
admin_mediamore_prefix = register.simple_tag(admin_mediamore_prefix)
