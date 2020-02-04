from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Item, ItemType, Review
from .forms import ReviewCreateForm



def cart(request):
    template = 'goods/cart.html'
    context = {}
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
