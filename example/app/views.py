#!/usr/bin/env python

from django.shortcuts import render_to_response
from app.forms import ExampleForm


def home(req):
  return render_to_response(
    "index.html", {
      "form": ExampleForm()
    }
  )
