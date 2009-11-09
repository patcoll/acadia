from django.contrib import admin
from reversion.admin import VersionAdmin
from acadia.pages.models import Asset, Menu, Page, Template
from django.contrib.admin.util import unquote

class AssetAdmin(admin.ModelAdmin):
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

class MenuAdmin(admin.ModelAdmin):
    actions = None
    save_on_top = True
    list_display = ('title',)
    
    class Media:
        css = {
            "all": ("pages/css/menu.css",)
        }
        
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        obj = self.queryset(request).get(pk=unquote(object_id))
        my_context = {
            'xml': obj.get_xml(),
        }
        return super(MenuAdmin, self).change_view(request, object_id, 
            extra_context=my_context)
admin.site.register(Menu, MenuAdmin)

class PageAdmin(VersionAdmin):
    save_as = True
    # revision_form_template = "admin/pages/page/revision_form.html"
    # object_history_template = "admin/pages/page/object_history.html"
    change_list_template = "admin/pages/page/reversion/change_list.html"
    # recover_list_template = "admin/pages/page/recover_list.html"
    # recover_form_template = "admin/pages/page/recover_form.html"
    search_fields = ('title', 'content')
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