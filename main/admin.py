from django.contrib import admin
from models import *

class AssetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Asset, AssetAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('title',)}
admin.site.register(Page, PageAdmin)
