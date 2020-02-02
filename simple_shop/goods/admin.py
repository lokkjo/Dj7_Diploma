from django.contrib import admin



from .models import Item, ItemType, Review
# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'type', 'add_time')
    prepopulated_fields = {"name_slug": ("name",)}
    fieldsets = [
        (None,               {'fields': ['name', 'image',
                                         'description', 'type']}),
        ('Date information', {'fields': ['add_time'],
                              'classes': ['collapse']}),
        ('Tech info',        {'fields': ['name_slug'],
                              'classes': ['collapse']})
    ]
    inlines = [
        ReviewInline
    ]

class ItemTypeAdmin(admin.ModelAdmin):
    model = ItemType





admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)