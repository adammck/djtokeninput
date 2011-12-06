jQuery Tokeninput for Django
============================

This is reusable Django app which provides `TokenField` as a drop-in replacement for `ModelMultipleChoiceField`. It wraps the excellent [jQuery Tokeninput] (https://github.com/loopj/jquery-tokeninput) plugin, which is by [James Smith] (http://loopj.com).


Quick Start
-----------

I haven't packaged this yet, so install it via GitHub for now:

```bash
$ pip install -e git://github.com/adammck/djtokeninput.git#egg=djtokeninput
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
  "django.contrib.contenttypes",
  "djtokeninput",
  # ...
)
```

Add the generic search view to your `urlpatterns`:

```python
urlpatterns = patterns("",
  # ...
  url(r"^djtokeninput/", include("djtokeninput.urls"))
)
```

Add a `search` method to your model:

```python
from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=100)

  @classmethod
  def search(cls, query):
    return cls.objects.filter(name__icontains=query)
```

Add a `TokenField` to your form:

```python
from django import forms
from djtokeninput import TokenField

class ExampleForm(forms.Form):
  title = forms.CharField()
  desc = forms.CharField(widget=forms.Textarea)
  tags = TokenField(models.Tag, required=False)
```

Finally, add the JS and CSS assets to your template:

```html
<head>
  <link rel="stylesheet" href="/static/css/token-input.css">
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  <script src="/static/js/jquery-tokeninput-1.6.0-min.js"></script>
  <script src="/static/js/djtokeninput.js"></script>
</head>
```


Form Media
----------

You can also use [Form Media] (https://docs.djangoproject.com/en/dev/topics/forms/media) if you're into that. Just include `{{ form.media }}` in your `<head>` as usual.

I prefer to explicity include all of my assets in my base template, and pack them with [Django Compressor] (https://github.com/jezdez/django_compressor).


Configuration
-------------

You can configure the Tokeninput by passing a `TokenWidget` instance to `TokenField`:

```python
tags = TokenField(models.Tag, required=False,
  widget=TokenWidget(
    hint_text="Search for tags",
    prevent_duplicates=True,
    animate_dropdown=False))
```

The [jQuery Tokeninput docs] (http://loopj.com/jquery-tokeninput/#configuration) contains the list of available settings.


Requirements
------------

  * Django `>= 1.3`
  * jQuery `>= 1.5`


License
-------

[djtokeninput](https://github.com/adammck/djtokeninput) is free software, available under the MIT license.
