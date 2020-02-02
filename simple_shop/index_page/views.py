from django.shortcuts import render

from .models import Offer
from goods.models import Item

# Create your views here.

def index(request):
    template = 'goods/index.html'
    items = Item.objects.all().prefetch_related()
    offers = Offer.objects.all().prefetch_related().values().order_by('-add_date')[:3]

    context = {
               'items': items,
               'offers': offers
    }
    return render(request, template, context)