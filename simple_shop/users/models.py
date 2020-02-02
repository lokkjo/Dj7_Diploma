from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone

# from goods.models import Item

class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('goods.Item', through='OrderPosition')
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey('goods.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'