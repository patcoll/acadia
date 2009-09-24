from django.contrib import admin
from reversion.admin import VersionAdmin
from models import *

class PageAdmin(VersionAdmin):
    list_display = ('title', 'published', 'modified')
    fieldsets = (
        (None, {
            'fields': ('title', 'content',)
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
    fieldsets = (
        ('Editor dimensions', {
            'fields': ('editor_width', 'editor_height',)
        }),
    )

admin.site.register(Template, TemplateAdmin)