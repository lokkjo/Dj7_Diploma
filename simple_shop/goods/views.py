from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


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

def phones(request):
    template = 'goods/smartphones.html'
    phones = Item.objects.all().prefetch_related().filter(type=1).order_by('-add_time')
    context = {'phones': phones}
    return render(request, template, context)

def accessoires(request):
    template = 'goods/accessoires.html'
    accessoires = Item.objects.all().prefetch_related().filter(type=2).order_by('-add_time')
    context = {'accessoires': accessoires}
    return render(request, template, context)
    # return HttpResponse('accessoires collection')

def item_page(request, name_slug):
    item_string = request.GET.get('name_slug')
    print(item_string)
    return HttpResponse(f'item page: {name_slug}')

