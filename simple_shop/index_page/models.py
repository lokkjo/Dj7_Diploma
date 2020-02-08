from django.db import models

from django.utils import timezone as tz


class Offer(models.Model):
    """
    Модель для рекламной статьи с выборкой товаров на главной
    """
    headline = models.CharField(max_length=200, verbose_name='заголовок')
    sub_line = models.CharField(max_length=300, verbose_name='саблайн')
    category = models.ForeignKey('goods.ItemType',
                                 on_delete=models.CASCADE, verbose_name='товары')
    add_date = models.DateTimeField(default=tz.now, verbose_name='дата создания')

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'


    def __str__(self):
        return self.headline
