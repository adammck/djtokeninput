#!/usr/bin/env python

import json
from django import forms
from django.core.urlresolvers import reverse


class TokenWidget(forms.TextInput):
  class Media:
    js = (
      "js/jquery-tokeninput-1.6.0-min.js",
      "js/token-widget.js"
    )

  def render(self, name, value, attrs=None):
    flat_value = ",".join(map(unicode, value or []))

    if hasattr(self, "search_view"):
      attrs["data-search-url"] = reverse(self.search_view)

    attrs["class"] = self._class_name(
      attrs.get("class"), "token-input")

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
