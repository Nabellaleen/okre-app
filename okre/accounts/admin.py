from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom admin class for the User model.
    """
    # The fields to be used in displaying the User model
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # The fields to be used when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # The fields to be displayed in the user list view
    list_display = ('email', 'is_staff')
    # The fields to be used for searching the user list
    search_fields = ('email',)
    # The fields to be used for filtering the user list
    ordering = ('email',)
