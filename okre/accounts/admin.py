from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from common.admin_mixins import ConfigurableRelatedFieldWidgetMixin

from .models import User

class UserOrganizationInline(ConfigurableRelatedFieldWidgetMixin, admin.TabularInline):
    """
    Inline admin class for the Team model with is_organization=True.
    This class is used to display the organizations associated with a user.
    """
    model = User.organizations.through
    extra = 0

    verbose_name = "Organization"
    verbose_name_plural = "Organizations"

    INLINE_RELATED_CONFIG = {
        'team': {
            'can_add_related': False,
            'can_change_related': False,
        },
    }

    def get_queryset(self, request):
        """
        Override the get_queryset method to filter teams based on the is_organization field.
        """
        qs = super().get_queryset(request)
        return qs.filter(team__is_organization=True)


class UserTeamInline(ConfigurableRelatedFieldWidgetMixin, admin.TabularInline):
    """
    Inline admin class for the Team model with is_organization=False.
    This class is used to display the teams associated with a user.
    """
    model = User.organizations.through
    extra = 0

    verbose_name = "Team"
    verbose_name_plural = "Teams"

    INLINE_RELATED_CONFIG = {
        'team': {
            'can_add_related': False,
            'can_change_related': False,
        },
    }

    def get_queryset(self, request):
        """
        Override the get_queryset method to filter teams based on the is_organization field.
        """
        qs = super().get_queryset(request)
        return qs.filter(team__is_organization=False)


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
    # The inlines tables to be displayed in the user admin page
    inlines = [UserOrganizationInline, UserTeamInline]
    # The fields to be displayed in the user list view
    list_display = ('email', 'is_staff')
    # The fields to be used for searching the user list
    search_fields = ('email',)
    # The fields to be used for filtering the user list
    ordering = ('email',)
