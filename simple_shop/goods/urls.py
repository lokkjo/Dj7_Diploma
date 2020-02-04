from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('item/<str:name_slug>/', views.item_page, name='item_page'),
    path('cart/', views.cart, name='cart'),
    # path('login/', views.login, name='login'),
    path('<str:item_type>/', views.items_by_category, name='category'),
]