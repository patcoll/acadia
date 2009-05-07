import os
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings
import mptt, tagging
import tagging.fields

# assert False, settings.SITE_SETTINGS.admin_email

# ==========
# = Models =
# ==========
class Asset(models.Model):
  creator = models.ForeignKey(User)
  # active = models.BooleanField(default=True)
  file_name = models.FileField(upload_to=settings.ASSETS, max_length=255)
  title = models.CharField(max_length=255)
  tags = tagging.fields.TagField()
  created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
  modified = models.DateTimeField(auto_now=True, editable=False, null=True)
  
  def __unicode__(self):
    return self.file_name
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

class Navigation(models.Model):
  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = generic.GenericForeignKey('content_type', 'object_id')
  
  def __unicode__(self):
    return self.content_object
mptt.register(Navigation)

class Page(models.Model):
  template = models.ForeignKey('Template')
  user = models.ForeignKey(User)
  active = models.BooleanField(default=True)
  name = models.SlugField(max_length=255)
  title = models.CharField(max_length=255)
  content = models.TextField(help_text="You may use Markdown here.")
  # blocks = generic.GenericRelation('SiteBlock')
  created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
  modified = models.DateTimeField(auto_now=True, editable=False, null=True)
  
  def __unicode__(self):
    return self.title

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
  blocks = generic.GenericRelation('SiteBlock')
  editor_width = models.PositiveIntegerField(default=600)
  editor_height = models.PositiveIntegerField(default=700)
  
  def __unicode__(self):
    return self.name


# =============================
# = Register models with apps =
# =============================
