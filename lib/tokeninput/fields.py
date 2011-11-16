#!/usr/bin/env python

from django import forms
from djtokeninput.widgets import TokenWidget


class TokenField(forms.ModelMultipleChoiceField):
  widget = TokenWidget

  @staticmethod
  def _class_name(value):
    return value.replace(" ", "-")

  def __init__(self, model, search_view, *args, **kwargs):
    super(TokenField, self).__init__(model.objects.all(), *args, **kwargs)
    self.widget.class_name = self._class_name(model._meta.verbose_name_plural)
    self.widget.search_view = search_view
