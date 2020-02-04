from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

# from users.models import User

goods_fs = FileSystemStorage(str(Path('media/photos')))


class Item(models.Model):
    name = models.CharField(max_length=64)
    # image = models.ImageField(storage=goods_fs)
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

