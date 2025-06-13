# Copyright (C) 2025  Florian Briand (Digital Engine)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from django.contrib import admin
from django.utils.html import format_html_join

from common.admin_mixins import ConfigurableRelatedFieldWidgetMixin
from okr.models import Objective

from .models import Team

class TeamInline(admin.TabularInline):
    """
    Inline admin class for the Team model.
    """
    model = Team
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    extra = 0
    fk_name = 'parent'

    verbose_name = "Team"
    verbose_name_plural = "Teams"


class TeamMemberInline(ConfigurableRelatedFieldWidgetMixin, admin.TabularInline):
    """
    Inline admin class for the TeamMember model.
    """
    model = Team.members.through
    fields = ('user',)
    extra = 0

    verbose_name = "Member"
    verbose_name_plural = "Members"

    INLINE_RELATED_CONFIG = {
        'user': {
            'can_add_related': False,
            'can_change_related': False,
        },
    }

class TeamObjectivesInline(admin.StackedInline):
    """
    Inline admin class for the Objectives model.
    """
    model = Objective
    fields = ('title', 'description', 'key_results_list')
    readonly_fields = ('key_results_list',)
    extra = 0
    
    show_change_link = True
    
    def key_results_list(self, obj):
        print("-----")
        key_results = obj.key_results.all()
        if not key_results:
            return "No Key Results"
        return format_html_join(
            '\n',
            '<li>{}</li>',
            [(str(kr),) for kr in key_results]
        )



@admin.register(Team)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Admin class for the Team model of type Organization.
    """
    model = Team
    fields = ('name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('is_organization',)
    search_fields = ('name',)
    inlines = [TeamInline, TeamMemberInline, TeamObjectivesInline]

    def get_queryset(self, request):
        """
        Override the get_queryset method to filter teams based on the is_organization field.
        """
        qs = super().get_queryset(request)
        return qs.filter(is_organization=True)
    
    def save_model(self, request, obj, form, change):
        """
        Override the save_model method to set the is_organization field to True.
        """
        if not obj.is_organization:
            obj.is_organization = True
        super().save_model(request, obj, form, change)
