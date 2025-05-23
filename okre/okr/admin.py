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
