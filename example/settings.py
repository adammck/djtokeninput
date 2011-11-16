#!/usr/bin/env python

import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)


DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "%s/db.sqlite3" % PROJECT_ROOT
  }
}

INSTALLED_APPS = (
  'django.contrib.staticfiles',
  "tokeninput",
  "app"
)

STATICFILES_FINDERS = (
  "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

ROOT_URLCONF = "example.urls"
STATIC_URL = "/static/"
DEBUG = True
