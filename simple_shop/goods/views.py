from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, ItemType


def index(request):
    template = 'goods/index.html'
    items = Item.objects.all().prefetch_related()
    phones = items.filter(type=1).order_by('add_time')[:3]
    # print('phones: ', phones)
    accessoires = items.filter(type=2)[:3]
    # print('accs', accessoires)
    context = {'phones': phones,
               'accessoires': accessoires}
    return render(request, template, context)

def login(request):
    template = 'goods/login.html'
    context = {}
    return render(request, template, context)

def cart(request):
    template = 'goods/cart.html'
    context = {}
    return render(request, template, context)

# def phones(request):
#     template = 'goods/smartphones.html'
#     phones = Item.objects.all().prefetch_related()\
#         .filter(type=1).order_by('-add_time')
#     context = {'phones': phones}
#     return render(request, template, context)
#
# def accessoires(request):
#     template = 'goods/accessoires.html'
#     accessoires = Item.objects.all().prefetch_related()\
#         .filter(type=2).order_by('-add_time')
#     context = {'accessoires': accessoires}
#     return render(request, template, context)
    # return HttpResponse('accessoires collection')

def items_by_category(request, item_type):
    page_num = int(request.GET.get('page', 1))
    count = 6
    template = 'goods/items_by_cat.html'
    items = Item.objects.all().prefetch_related()\
        .filter(type__item_type=item_type).order_by('-add_time')
    category = ItemType.objects.all().filter(item_type=item_type)
    paginator = Paginator(items, count)
    page = paginator.get_page(page_num)
    context = {
        'items': items,
        'category': category,
        'page': page
    }
    return render(request, template, context)

def item_page(request, name_slug):
    template = 'goods/item.html'
    position = Item.objects.all().prefetch_related()\
        .filter(name_slug=name_slug)
    context = {
        'position': position
    }
    return render(request, template, context)
