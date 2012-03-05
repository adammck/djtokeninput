#!/usr/bin/env python

from django import forms
from djtokeninput.fields import TokenField, TokenWidget
from app import models


class ExampleForm(forms.Form):
  title = forms.CharField()
  desc = forms.CharField(widget=forms.Textarea)
  tags = TokenField(models.Tag, required=False,
    widget=TokenWidget(prevent_duplicates=True),
    help_text='Try searching for "alpha", "beta", etc.')
