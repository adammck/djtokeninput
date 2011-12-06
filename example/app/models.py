#!/usr/bin/env python

from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name

  @classmethod
  def search(cls, query):
    return cls.objects.filter(name__icontains=query)

  @classmethod
  def create_via_tokeninput(cls, value):
    return cls.objects.create(name=value.strip())


class Post(models.Model):
  title = models.CharField(max_length=100)
  tags = models.ManyToManyField(Tag, blank=True)
