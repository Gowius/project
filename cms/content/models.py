# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_model
import random
from django.conf import settings
from content.fields import *
from mptt.models import MPTTModel, TreeForeignKey
import datetime




def make_upload_path(instance, filename, prefix = False):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0,10000)
    n2 = random.randint(0,10000)
    n3 = random.randint(0,10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Меню"


class MenuItem(MPTTModel):
    menu = models.ForeignKey(Menu,null=True, blank=True, verbose_name="Меню")
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Родительский пункт меню")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Пункты меню"
    class MPTTMeta:
        order_insertion_by = ['name']


class Category(MPTTModel):
    name = models.CharField(max_length=250, verbose_name="Название")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Родительская категория")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by = ['name']

class Article(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    image = ThumbnailImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение")
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name="Категория")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    metaKey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metaDesc = models.CharField(max_length=250, blank=True, verbose_name="Описание")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    short_text = tinymce_model.HTMLField(blank=True, verbose_name="Короткое описание")
    full_text = tinymce_model.HTMLField(blank=True, verbose_name="Полное описание")
    pub_date = models.DateField( default=datetime.date.today(), blank=True, verbose_name="Дата публикации")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Страницы"

class Snipet(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    text = tinymce_model.HTMLField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Куски кода"
        verbose_name = "Снипет"
