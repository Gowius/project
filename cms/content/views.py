# -*- coding: utf-8 -*-
from django.db import models
from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.shortcuts import redirect, render, get_object_or_404
from content.models import *



def clear_cache(request):
    cache.clear()
    return redirect('/')

def my_404_view(request):
    template = loader.get_template('404.html')
    context = Context({
        'request': request,
        })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

def home(request):
    return render(request, 'index.html', {})
