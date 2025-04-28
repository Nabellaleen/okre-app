from django.contrib import admin

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
    inlines = [TeamInline]

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
