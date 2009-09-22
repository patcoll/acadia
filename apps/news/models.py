import os
from django.db import models
from django.contrib.auth.models import User
from tagging.models import Tag
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings
import mptt, tagging
import tagging.fields


class NewsPost(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    name = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="You may use Markdown here.")