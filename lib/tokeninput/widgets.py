#!/usr/bin/env python

import json
from django import forms
from django.core.urlresolvers import reverse


class TokenWidget(forms.TextInput):
  class Media:
    css = {
      "all": ("css/token-input.css",)
    }

    js = (
      "js/jquery-tokeninput-1.6.0-min.js",
      "js/djtokeninput.js"
    )

  @staticmethod
  def _class_name(value):
    return value.replace(" ", "-")

  def render(self, name, value, attrs=None):
    flat_value = ",".join(map(unicode, value or []))

    url_name = getattr(self, "search_url", "djtokeninput_search")
    url_args = (self.model._meta.app_label, self.model._meta.object_name.lower())
    attrs["data-search-url"] = reverse(url_name, args=url_args)

    attrs["class"] = self._class_name(
      attrs.get("class"), "tokeninput")

    if value is not None:
      attrs["data-prepopulate"] = json.dumps([
        {"id": pk, "name": unicode(self.choices.queryset.get(pk=pk))}
        for pk in value
      ])

    return super(TokenWidget, self).render(name, flat_value, attrs)

  @staticmethod
  def _class_name(class_name=None, extra=None):
    return " ".join(filter(None, [class_name, extra]))

  def value_from_datadict(self, data, files, name):
    values = data.get(name, "").split(",")
    return self.clean_keys(values)

  def clean_keys(self, values):
    return [int(x) for x in values if x.strip().isdigit()]
