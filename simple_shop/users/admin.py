# User customization asset from
# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Define admin model for custom User model with no email field
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser','groups',
                                       'user_permissions'),
                            'classes': ['collapse']}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined'),
                                'classes': ['collapse']})
    )
    add_fieldsets = (
        (None, {
            'classes':['wide',],
            'fields': ['email','first_name', 'last_name',
                       'password1', 'password2',],
        }),
    )

    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


