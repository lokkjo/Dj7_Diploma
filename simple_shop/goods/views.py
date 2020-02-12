from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.db.models import ObjectDoesNotExist

from .models import Item, ItemType, Review, Order
from .forms import ReviewCreateForm

CATEGORY_ITEMS_COUNT = 6 # Items for page in items_by_category view



@login_required
def cart(request):
    """
    Страница корзины. Считывает из запроса (request) поля
    'order_id' (id заказа) и 'position_id' (id товара, добавляемого
    в корзину).
    """
    template = 'goods/cart.html'

    if request.method == 'GET':
        order_id = request.session.get('order_id')
        order = Order.objects.prefetch_related().get(
            id=order_id, is_closed=False
        )
        context = {'order': order}
        return render(request, template, context)

    if request.method == 'POST':
        pos_id = request.POST.get('position_id')

        user = request.user
        position = Item.objects.prefetch_related().get(id=pos_id)
        order_id = request.session.get('order_id')
        try:
            order = Order.objects.prefetch_related().get(
                id=order_id, is_closed=False
            )
        except ObjectDoesNotExist:
            order = Order.objects.create(buyer=user)
            request.session['order_id'] = f'{order.id}'

        try:
            pos_record = order.orderposition_set.get(
                item_id=pos_id
            )
            pos_record.quantity = pos_record.quantity + 1
            pos_record.save()
        except ObjectDoesNotExist:
            order.items.add(position)
            order.save()

        return HttpResponseRedirect(reverse('goods:cart'))



def success_order(request):
    """
    Страница завершения заказа. Считывает из request поле 'order_id'
    с идентификатором заказа. Закрывает заказ, делает его недоступным
    для дальнейшего наполнения.
    """
    template = 'goods/success_order.html'
    order_id = request.session.get('order_id')
    context = {'order_id': order_id}
    order_record = Order.objects.filter(
        id=order_id,
    )
    order_record.update(is_closed=True)
    request.session.pop('order_id')

    return render(request, template, context)



def items_by_category(request, item_type_slug):
    """
    Страница категории с пагинацией
    :param request: стандартный запрос
    :param item_type_slug: идентификатор категории,
        соответствует полю models.ItemType.item_type
    """
    page_num = int(request.GET.get('page', 1))
    count = CATEGORY_ITEMS_COUNT
    template = 'goods/items_by_cat.html'
    items = Item.objects.all().prefetch_related('type')\
        .filter(type__slug=item_type_slug).order_by('-add_time')
    category = items.first().type.display_name
    print('cat is:', category)
    paginator = Paginator(items, count)
    page = paginator.get_page(page_num)
    context = {
        'items': items,
        'category': category,
        'page': page
    }
    return render(request, template, context)

def item_page(request, name_slug):
    """
    Страница наименования товара
    :param request: стандартный запрос
    :param name_slug: слагифицированное наименование товара,
        соответствует полю models.Item.name_slug
    """
    template = 'goods/item.html'
    position = Item.objects.all().get(name_slug=name_slug)

    if request.method == 'POST':
        review_form = ReviewCreateForm(request.POST)
        if review_form.is_valid():
            text = review_form.cleaned_data['text']
            rating = review_form.cleaned_data['rating']
            author = request.user
            new_review = Review.objects.create(
                author=author, item=position,
                text=text, rating=rating
            )
            return redirect('goods:item_page', f'{name_slug}')
    else:
        review_form = ReviewCreateForm()

    context = {
        'position': position,
        'form': review_form,
    }
    return render(request, template, context)
