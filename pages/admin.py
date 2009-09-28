from django.contrib import admin
from reversion.admin import VersionAdmin
from models import *

class AssetAdmin(admin.ModelAdmin):
    # pass
    list_display = ('__unicode__', 'active')
    fieldsets = (
        (None, {
            'fields': ('file_name', 'title', 'tags')
        }),
    )
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
admin.site.register(Asset, AssetAdmin)

class PageAdmin(VersionAdmin):
    list_display = ('title', 'published', 'modified')
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('name',)
        }),
    )
    prepopulated_fields = {'name': ('title',)}
    exclude = ('published', 'template', 'user')
    include = ('title', 'name', 'content')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
admin.site.register(Page, PageAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'editor_width', 'editor_height')
    fieldsets = (
        ('Editor dimensions', {
            'fields': ('editor_width', 'editor_height')
        }),
    )

admin.site.register(Template, TemplateAdmin)