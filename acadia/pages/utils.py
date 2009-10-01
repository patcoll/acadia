
def content_type_slug_for_obj(obj):
    from django.contrib.contenttypes.models import ContentType
    ct = ContentType.objects.get_for_model(obj)
    return "%s_%s" % (ct.app_label, ct.model)
    