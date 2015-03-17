#!/usr/bin/env python

from django.conf.urls import patterns, url, include




urlpatterns = patterns("",
  url(r"^$", "example.app.views.home", name="home"),
  url(r"^djtokeninput/", include("djtokeninput.urls"))
)
