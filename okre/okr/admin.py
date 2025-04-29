from django.contrib import admin

from .models import Objective

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
