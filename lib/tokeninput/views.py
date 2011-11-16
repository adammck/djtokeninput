#!/usr/bin/env python

import json
from django import http
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


def _tokens(query_set, keys=("id", "name")):
  return map(
    lambda v: dict(zip(keys, v)),
    query_set.values_list(*keys))

def search(req, app_label, model):
  content_type = get_object_or_404(ContentType, app_label=app_label, model=model)
  model = content_type.model_class()

  if hasattr(model, "search"):
    if "q" in req.GET:
      query_set = model.search(req.GET["q"])
      tokens = _tokens(query_set)

    else:
      tokens = []

    return http.HttpResponse(
      json.dumps(tokens),
      content_type="application/json")

  else:
    raise http.Http404
