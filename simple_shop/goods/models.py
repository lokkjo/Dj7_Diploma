from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.db import models

# Create your models here.
from django.utils import timezone

# from users.models import User


class Item(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=400)
    type = models.ForeignKey('ItemType', on_delete=models.CASCADE)
    review = models.ManyToManyField('users.User', through='Review',
                                    related_name='items')
    name_slug = models.SlugField()
    add_time = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name


class ItemType(models.Model):
    item_type = models.CharField(max_length=32)
    name = models.CharField(max_length=32, default='NewName')

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товара'

    def __str__(self):
        return self.item_type


class Review(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    reviewed_item = models.ForeignKey(Item, on_delete=models.CASCADE,
                                      related_name='reviews')
    review_text = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(
        default=1,validators=[MinValueValidator(1),
                              MaxValueValidator(5)]
    )


class Order(models.Model):
    buyer = models.ForeignKey('users.User', on_delete=models.CASCADE,
                              verbose_name='покупатель')
    items = models.ManyToManyField(Item, through='OrderPosition')
    date = models.DateTimeField(default=timezone.now,
                                verbose_name='дата создания')
    is_closed = models.BooleanField(default=False,
                                    verbose_name='сформирован')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f"Заказ № {self.pk}"


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'

    def __str__(self):
        return f"{self.item}, {self.quantity} шт."