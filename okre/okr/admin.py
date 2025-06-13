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

from .models import Objective, KeyResult


class KeyResultInline(admin.StackedInline):
    """
    Inline admin class for KeyResult model to display within Objective admin.
    """
    model = KeyResult
    extra = 0


@admin.register(Objective)
class ObjectivesAdmin(admin.ModelAdmin):
    """
    Admin class for the Objectives model.
    """
    list_display = ('title', 'team', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('team',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    inlines = [KeyResultInline]
