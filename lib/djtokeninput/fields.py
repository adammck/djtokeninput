#!/usr/bin/env python

from django import forms
from djtokeninput.widgets import TokenWidget


class TokenField(forms.ModelMultipleChoiceField):
  kwargs_for_widget = ("search_url",)
  widget = TokenWidget

  @staticmethod
  def _class_name(value):
    return value.replace(" ", "-")

  def __init__(self, model, *args, **kwargs):
    widget_attrs = { }

    for name in self.kwargs_for_widget:
      if name in kwargs:
        widget_attrs[name] = kwargs.pop(name)

    super(TokenField, self).__init__(model.objects.all(), *args, **kwargs)
    self.widget.class_name = self._class_name(model._meta.verbose_name_plural)
    self.widget.model = model

    for name in widget_attrs:
      setattr(self.widget, name, widget_attrs[name])
