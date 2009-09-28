import os.path
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings

import mptt
import tagging
import tagging.fields
from tagging.models import Tag

# from django.core.files.storage import FileSystemStorage
# ASSETS = FileSystemStorage(location=settings.ASSETS)

class Asset(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    mime_type = models.CharField(max_length=255)
    file_name = models.FileField(upload_to='assets', max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    tags = tagging.fields.TagField()
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modified = models.DateTimeField(auto_now=True, editable=False, null=True)

    class Meta:
        ordering = ('file_name',)
        verbose_name = 'asset'
        verbose_name_plural = 'assets'

    def __unicode__(self):
        return os.path.basename(self.file_name.name)

    def get_absolute_url(self):
        return "%sassets/%s" % (settings.MEDIA_URL, self.file_name)

    # def set_tags(self, tags):
    #     Tag.objects.update_tags(self, tags)
    # 
    # def get_tags(self):
    #     return Tag.objects.get_for_object(self)
tagging.register(Asset)

# class Block(models.Model):
#   block_type = models.ForeignKey('BlockType')
#   name = models.SlugField(max_length=255, unique=True)
#   title = models.CharField(max_length=255)
#   content = models.TextField()
#   created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
#   modified = models.DateTimeField(auto_now=True, editable=False, null=True)
#   
#   def __unicode__(self):
#     return self.name
# 
# class BlockType(models.Model):
#   name = models.SlugField(max_length=255, unique=True)
#   title = models.CharField(max_length=255)
#   editor_width = models.PositiveIntegerField(default=600)
#   editor_height = models.PositiveIntegerField(default=700)
#   
#   def __unicode__(self):
#     return self.name

# class Link(models.Model):
#   title = models.CharField(max_length=255)
#   url = models.URLField(max_length=255, unique=True)
#   created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
#   modified = models.DateTimeField(auto_now=True, editable=False, null=True)
#   
#   def __unicode__(self):
#     return self.url

# class Navigation(models.Model):
#   content_type = models.ForeignKey(ContentType)
#   object_id = models.PositiveIntegerField()
#   content_object = generic.GenericForeignKey('content_type', 'object_id')
#   
#   def __unicode__(self):
#     return self.content_object
# mptt.register(Navigation)

class Page(models.Model):
    template = models.ForeignKey('Template', default=lambda: Template.objects.get(name="interior").id)
    user = models.ForeignKey(User)
    published = models.BooleanField(default=True)
    name = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="You may use Markdown here.")
    # blocks = generic.GenericRelation('SiteBlock')
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modified = models.DateTimeField(auto_now=True, editable=False, null=True)
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'page'
        verbose_name_plural = 'pages'
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/%d/%s/" % (self.id, self.name)

# class Setting(models.Model):
#   name = models.SlugField(max_length=255, unique=True)
#   content = models.TextField()
#   
#   def __unicode__(self):
#     return self.name

# class SiteBlock(models.Model):
#   block = models.ForeignKey(Block)
#   content_type = models.ForeignKey(ContentType)
#   object_id = models.PositiveIntegerField()
#   content_object = generic.GenericForeignKey('content_type', 'object_id')
#   order = models.PositiveIntegerField()
#   created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
#   modified = models.DateTimeField(auto_now=True, editable=False, null=True)
#   
#   def __unicode__(self):
#     return self.block.title

class Template(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    # blocks = generic.GenericRelation('SiteBlock')
    editor_width = models.PositiveIntegerField(default=600)
    editor_height = models.PositiveIntegerField(default=700)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'template'
        verbose_name_plural = 'templates'
    
    def __unicode__(self):
        return self.name


# signals
# import django.db.models.signals

