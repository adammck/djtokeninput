#!/usr/bin/env python

from django.conf.urls import patterns, url, include


urlpatterns = patterns("",
  url(r"^(?P<app_label>\w+)/(?P<model>\w+)$", "djtokeninput.views.search", name="djtokeninput_search")
)
