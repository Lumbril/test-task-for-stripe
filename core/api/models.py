from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названние')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        db_table = 'items'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
