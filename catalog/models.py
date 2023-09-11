from django.db import models
from django.db.models import PROTECT


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='goods/', verbose_name='изображение ', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=PROTECT, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.price}, {self.category}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.pk}, {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
