from django.contrib import admin


from .models import Offer

class OfferAdmin(admin.ModelAdmin):
    model = Offer
    list_display = ('headline', 'category', 'add_date')


admin.site.register(Offer, OfferAdmin)