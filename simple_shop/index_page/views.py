from django.shortcuts import render

from .models import Offer
from goods.models import Item

OFFER_ITEMS_COUNT = 3

def index(request):
    """
    Главная страница
    """
    template = 'goods/index.html'
    # items = Item.objects.all().prefetch_related('type')
    items = Item.objects.all()
    offers = Offer.objects.all().values()\
        .order_by('-add_date')[:OFFER_ITEMS_COUNT]
    context = {'items': items,
               'offers': offers}
    return render(request, template, context)
