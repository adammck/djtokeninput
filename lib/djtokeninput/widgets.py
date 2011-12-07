#!/usr/bin/env python

import re
import json
import copy
from django import forms
from django.core.exceptions import ObjectDoesNotExist
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

  def __init__(self, attrs=None, **kwargs):
    super(TokenWidget, self).__init__(attrs)
    self.settings = self._normalize(kwargs)

  @classmethod
  def _normalize(cls, settings):
    """
    Return a copy of `settings` (a dict) with any underscored keys replaced
    with camelCased keys. Useful for passing Python-style dicts to Tokeninput,
    which expects strange camelCase dicts.
    """

    return dict([
      (cls._camelcase(key), val)
      for key, val in settings.items()
    ])

  @staticmethod
  def _camelcase(s):
    return re.sub("_(.)", lambda m: m.group(1).capitalize(), s)

  @staticmethod
  def _class_name(value):
    return value.replace(" ", "-")

  def render(self, name, value, attrs=None):
    flat_value = ",".join(map(unicode, value or []))
    settings = copy.copy(self.settings)

    url_name = getattr(self, "search_url", "djtokeninput_search")
    url_args = (self.model._meta.app_label, self.model._meta.object_name.lower())
    attrs["data-search-url"] = reverse(url_name, args=url_args)

    attrs["class"] = self._class_name(
      attrs.get("class"), "tokeninput")

    if value is not None:
      prepop = []

      for pk in value:
        try:
          model = self.choices.queryset.get(pk=pk)
          prepop.append({ "id": pk, "name": unicode(model) })

        # Silently ignore invalid keys.
        except ObjectDoesNotExist:
          pass

      settings["prePopulate"] = prepop

    attrs["data-settings"] = json.dumps(settings)
    return super(TokenWidget, self).render(name, flat_value, attrs)

  @staticmethod
  def _class_name(class_name=None, extra=None):
    return " ".join(filter(None, [class_name, extra]))

  def value_from_datadict(self, data, files, name):
    flat_value = data.get(name, None)

    if not flat_value:
      return []

    values = flat_value.split(",")
    return self.clean_keys(values)

  def clean_key(self, value):
    try:
      return int(value)

    except ValueError:
      if hasattr(self.model, "create_via_tokeninput"):
        model = self.model.create_via_tokeninput(value)
        return model.pk

  def clean_keys(self, values):
    return filter(None, map(self.clean_key, values))
