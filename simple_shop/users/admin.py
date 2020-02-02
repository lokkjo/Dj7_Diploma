from django.contrib import admin

from .models import User, Order, OrderPosition
# Register your models here.

class OrderPositionInline(admin.TabularInline):
    model = OrderPosition

class UserAdmin(admin.ModelAdmin):
    model = User

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderPositionInline
    ]




admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)