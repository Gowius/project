# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from content.models import *
from django.utils.translation import to_locale, get_language, ugettext as _

def my_app_name(app_name):
    try:
        app = __import__(app_name.lower())
        return app.app_label
    except:
        return app_name

my_app_name = register.simple_tag(my_app_name)


@register.filter
def thumb(value):
    value = str(value)
    parts = value.split(".")
    parts.insert(-1, "thumb")
    return ".".join(parts)

@register.inclusion_tag('tags/snipet.html')
def snipet(id=1):
    from content.models import Snipet
    try:
        snipet = Snipet.objects.get(id=id)
    except:
        snipet = ''

    # assert False, snipet.text

    return {'snipet':snipet}
