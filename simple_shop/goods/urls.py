from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<str:name_slug>/', views.item_page, name='item_page'),
    path('phones/', views.phones, name='phones'),
    path('accessoires/', views.accessoires, name='accessoires'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart')
]