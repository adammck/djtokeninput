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
  url(r"^djtokeninput/", include("djtokeninput.urls")
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


Requirements
------------

  * Django `>= 1.3`
  * jQuery `>= 1.5`


License
-------

[djtokeninput](https://github.com/adammck/djtokeninput) is free software, available under the MIT license.
