from django.contrib import admin
from models import Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('template',)
admin.site.register(Page, PageAdmin)
