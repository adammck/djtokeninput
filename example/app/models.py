#!/usr/bin/env python

from django import forms
from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name

  @classmethod
  def search(cls, query):
    return cls.objects.filter(name__icontains=query)


class Post(models.Model):
  title = models.CharField(max_length=100)
  tags = models.ManyToManyField(Tag, blank=True)
