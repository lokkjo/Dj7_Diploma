from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Item(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='static/images/')
    description = models.CharField(max_length=400)
    type = models.ForeignKey('ItemType', on_delete=models.CASCADE)
    review = models.ManyToManyField(User, through='Review')
    name_slug = models.SlugField()
    add_time = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_item = models.ForeignKey(Item, on_delete=models.CASCADE,
                                      related_name='item')
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

class ItemType(models.Model):
    item_type = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товара'

    def __str__(self):
        return self.item_type