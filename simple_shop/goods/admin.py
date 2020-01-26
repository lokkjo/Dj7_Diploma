from django.contrib import admin



from .models import User, Item, ItemType
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'type', 'add_time')
    prepopulated_fields = {"name_slug": ("name",)}
    fieldsets = [
        (None,               {'fields': ['name', 'image',
                                         'description']}),
        ('Date information', {'fields': ['add_time'],
                              'classes': ['collapse']}),
        ('Tech info',        {'fields': ['type', 'name_slug'],
                              'classes': ['collapse']})
    ]



class ItemTypeAdmin(admin.ModelAdmin):
    model = ItemType

admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)