#!/usr/bin/env python

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("",
  url(r"^$", "example.app.views.home", name="home"),
  url(r"^tags$", "example.app.views.tags", name="search_tags")
)
