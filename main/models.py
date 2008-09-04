import os
from django.db import models
from django.contrib.auth.models import User
from django import newforms as forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings

# ==========
# = Models =
# ==========
class Asset(models.Model):
    user = models.ForeignKey(User, editable=False)
    active = models.BooleanField(default=True)
    file_name = models.FileField(upload_to=os.path.join(settings.FRONT_END, 'assets'), max_length=255)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.file_name

class Block(models.Model):
    block_type = models.ForeignKey('BlockType')
    name = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.name

class BlockType(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    mock_template = models.BooleanField()
    editor_width = models.IntegerField(default=600)
    editor_height = models.IntegerField(default=700)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.name

class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.url

class NavNode(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_set')
    lft = models.IntegerField(blank=True, null=True, editable=False)
    rght = models.IntegerField(blank=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.content_object
    
class Navigation(NavNode):
    pass

class NotInNavigation(NavNode):
    pass

class Page(models.Model):
    template = models.ForeignKey('Template')
    published_version = models.ForeignKey('PageVersion', related_name='published_version')
    active = models.BooleanField(default=True)
    name = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    blocks = generic.GenericRelation('SiteBlock')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.title

class PageVersion(models.Model):
    page = models.ForeignKey(Page)
    user = models.ForeignKey(User, editable=False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

class Setting(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.name

class SiteBlock(models.Model):
    block = models.ForeignKey(Block)
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.block.title

class Tag(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.title

class Template(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    blocks = generic.GenericRelation('SiteBlock')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __unicode__(self):
        return self.name


# =========================
# = Custom Admin Settings =
# =========================
from django.contrib import admin

class AssetAdmin(admin.ModelAdmin):
    fields = ('file_name', 'title', 'active')


class PageContentInline(admin.StackedInline):
    model = PageVersion
    extra = 1
class PageAdmin(admin.ModelAdmin):
    fields = ('title', 'name', 'template')
    prepopulated_fields = {'name': ('title',)}
    inlines = [PageContentInline]


admin.site.register(Asset, AssetAdmin)
admin.site.register(Page, PageAdmin)





# 
# 
# 
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     tags = models.ManyToManyField(Tag)
# 
# class Comment(models.Model):
#     post = models.ForeignKey(Post)
#     user = models.ForeignKey(User)
#     content = models.TextField()
#
