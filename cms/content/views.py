# -*- coding: utf-8 -*-
from django.db import models
from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.shortcuts import redirect, render, get_object_or_404
from content.models import *
from shop.models import Product, Seo, SeoBrand, LowPrice, Popular
from slideshow.models import *

def clear_cache(request):
    cache.clear()
    return redirect('/')


def home(request):
    saleslider = Product.objects.filter(saleslider = True).order_by('?')[:8]
    recomend = Product.objects.filter(recomend = True).order_by('?')[:8]
    from shop.models import Category
    cat = Category.objects.filter(published=True).order_by('ordering')

    slides = Slid.objects.filter(category_id = 1, published = True).order_by('ordering')
    banners = Slid.objects.filter(category_id = 2, published = True).order_by('ordering')

    # seo = Seo.objects.all().order_by('?')[:5]
    seo_brand = SeoBrand.objects.all().order_by('?')[:7]
    popular = Popular.objects.all().order_by('?')[:7]
    nedorogo = LowPrice.objects.all().order_by('?')[:7]
    left_column = []
    i = 0
    for item in seo_brand:
        # left_column.append(seo[i])
        left_column.append(seo_brand[i])
        left_column.append(popular[i])
        left_column.append(nedorogo[i])
        i += 1

    return render(request, 'index.html', {
        'saleslider': saleslider,
        'recomend': recomend,
        'cat': cat,
        'slides': slides,
        'banners': banners,
        'left_column': left_column,
        })

def page(request, slug):
    page = get_object_or_404(Article, slug=slug)
    return render(request, 'content/page.html', {'page':page})


def akcii(request):
    category = get_object_or_404(Category, slug='akcii')
    pages = Article.objects.filter(category=category)
    return render(request, 'content/akcii.html', {'pages':pages, 'category':category})

def akcya(request, slug):
    page = get_object_or_404(Article, slug=slug)
    return render(request, 'content/akcya.html', {'page':page})
