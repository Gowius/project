from django.contrib import admin
from django.db import models

from content.models import *
from content.fields import AdminImageWidget


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'menu', 'slug', 'published', 'ordering')
    list_editable = ('slug', 'published', 'ordering')
admin.site.register(MenuItem, MenuItemAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug', 'category', 'slug', 'published', 'ordering')
    list_editable = ('slug', 'published', 'ordering')
admin.site.register(Article, ArticleAdmin)


class InlineMenuItem(admin.StackedInline):
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_editable = ('name',)
    inlines = [InlineMenuItem]
admin.site.register(Menu, MenuAdmin)

admin.site.register(Category)
admin.site.register(Snipet)
