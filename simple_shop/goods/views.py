from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.db.models import ObjectDoesNotExist

from .models import Item, ItemType, Review, Order
from .forms import ReviewCreateForm


@login_required
def cart(request):
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

        print('from cart', pos_id)

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
    template = 'goods/success_order.html'
    order_id = request.session.get('order_id')
    order_record = Order.objects.filter(
        id=order_id,
    )
    for order in order_record:
        order.is_closed = True
        order.save()

    context = {'order_id': order_id}
    return render(request, template, context)



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
    pos_id = []
    for content in position:
        pos_id.append(content)


    if request.method == 'POST':
        review_form = ReviewCreateForm(request.POST)
        if review_form.is_valid():
            review_text = review_form.cleaned_data['review_text']
            rating = review_form.cleaned_data['rating']
            # new_review = review_form.save(commit=False)
            author = request.user
            reviewed_item = pos_id[0]
            new_review = Review.objects.create(
                author=author, reviewed_item=reviewed_item,
                review_text=review_text, rating=rating
            )
            return redirect(f'/shop/item/{name_slug}/')
    else:
        review_form = ReviewCreateForm()

    context = {
        'position': position,
        'form': review_form,
    }
    return render(request, template, context)
