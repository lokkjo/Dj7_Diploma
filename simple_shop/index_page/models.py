from django.db import models

from django.utils import timezone as tz


from goods.models import Item, ItemType

# class OfferItemsManager(models.Manager):
#     def get_query_set(self):
#         return super().get_queryset().filter(category='Item__type_id')

class Offer(models.Model):
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

    # def selected_items(self):
    #     return super()