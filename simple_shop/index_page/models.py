from django.db import models

from django.utils import timezone as tz


from goods.models import Item, ItemType

# class OfferItemsManager(models.Manager):
#     def get_query_set(self):
#         return super().get_queryset().filter(category='Item__type_id')

class Offer(models.Model):
    headline = models.CharField(max_length=200)
    sub_line = models.CharField(max_length=300)
    category = models.ForeignKey('goods.ItemType',
                                 on_delete=models.CASCADE)
    add_date = models.DateTimeField(default=tz.now)


    def __str__(self):
        return self.headline

    def selected_items(self):
        return super()