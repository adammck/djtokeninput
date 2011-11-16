#!/usr/bin/env python

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("",
  url(r"^$", "example.app.views.home", name="home"),
  url(r"^djtokeninput/", include("djtokeninput.urls"))
)
