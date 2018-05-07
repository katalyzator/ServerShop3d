# coding=utf-8

from django.db import models
# Create your models here.
from django.db.models import Model


def image_upload_to(instance, filename):
    return "images/%s" % filename


class CategoryProduct(models.Model):
    active = models.BooleanField(verbose_name="Отобразить категорию", default=True)
    name = models.CharField(verbose_name="Категория", max_length=120, null=True)

    imgFir = models.ImageField(verbose_name="Обложка 1", null=True, help_text="512x512")
    imgSec = models.ImageField(verbose_name="Обложка 2", null=True, help_text="512x512")
    imgThi = models.ImageField(verbose_name="Обложка 3", null=True, help_text="512x512")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(verbose_name="Отобразить продукт", default=True)
    title = models.CharField(verbose_name="Назание", max_length=50, null=True)
    order = models.CharField(verbose_name="Цена", max_length=50, null=True)

    cover = models.ImageField(verbose_name="Обложка", null=True, help_text="1024x1024")

    description = models.CharField(verbose_name="Описание", max_length=320, null=True)
    category = models.ForeignKey(CategoryProduct, verbose_name="Категория")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title
