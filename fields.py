# from django.db.models import fields
# 
# class OrderField(fields.IntegerField):
#     """Ignores the incoming value and instead gets the maximum plus one of the field."""
#     def pre_save(self, model_instance, value):
#         # if the model is new and not an update
#         if model_instance.id is None:
#             # extra attaches a a "maximum" attribute to each record returned
#             records = model_instance.__class__.objects.extra(select={'maximum':'SELECT MAX("order") FROM %s' % model_instance._meta.db_table})
#             if records:
#                 # get the maximum attribute from the first record and add 1 to it
#                 value = records[0].maximum + 1
#             else:
#                 value = 1
#         # otherwise the model is updating, pass the attribute value through
#         else:
#             value = getattr(model_instance, self.attname)
#         return value
#     
#     # prevent the field from being displayed in the admin interface
#     def formfield(self, **kwargs):
#         return None