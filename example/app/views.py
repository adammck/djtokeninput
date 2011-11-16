#!/usr/bin/env python

import json
from django import http
from django.shortcuts import render_to_response
from app.forms import ExampleForm
from app.models import Tag


def home(req):
  return render_to_response(
    "index.html", {
      "form": ExampleForm()
    }
  )


def _tokens(query_set, keys=("id", "name")):
  return map(
    lambda v: dict(zip(keys, v)),
    query_set.values_list(*keys))

def _search(req, model):
  query_set = model.search(req.GET["q"])

  return http.HttpResponse(
    json.dumps(_tokens(query_set)),
    content_type="application/json")

def tags(req):
  return _search(req, Tag)
