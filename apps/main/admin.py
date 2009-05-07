from django.contrib import admin
from models import *

class AssetAdmin(admin.ModelAdmin):
  fields = ('file_name', 'title', 'tags')
  def save_model(self, request, obj, form, change):
    if not change:
      obj.user = request.user
    obj.save()
admin.site.register(Asset, AssetAdmin)

class PageAdmin(admin.ModelAdmin):
  prepopulated_fields = {'name': ('title',)}
admin.site.register(Page, PageAdmin)
