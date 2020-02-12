from django.contrib import admin

from .models import Item, ItemType, Review, Order, OrderPosition


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'type', 'add_time')
    prepopulated_fields = {"name_slug": ("name",)}
    fieldsets = [
        (None, {'fields': ['name', 'image',
                           'description', 'type']}),
        ('Date information', {'fields': ['add_time'],
                              'classes': ['collapse']}),
        ('Tech info', {'fields': ['name_slug'],
                       'classes': ['collapse']})
    ]
    inlines = [
        ReviewInline
    ]


class ItemTypeAdmin(admin.ModelAdmin):
    model = ItemType


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderPositionInline
    ]
    list_display = ('id', 'buyer', 'date', 'is_closed')
    search_fields = ('buyer', 'date', 'is_closed',)
    ordering = ('date', 'buyer',)


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Order, OrderAdmin)
