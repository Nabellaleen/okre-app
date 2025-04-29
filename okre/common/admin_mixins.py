
class ConfigurableRelatedFieldWidgetMixin:
    """
    A mixin class to configure the related field widget in the inline admin.
    This mixin should probably be used with Django's TabularInline or StackedInline classes.

    To configure the related field widget, set INLINE_RELATED_CONFIG
    in the subclass with the following structure:
    INLINE_RELATED_CONFIG = {
        '<Field Name>': {
            'can_add_related': <True/False>,
            'can_change_related': <True/False>,
        },
    }
    where field_name is the name of the field in the formset
    and can_add_related and can_change_related are booleans, defaulting to True

    Example:
        class ExampleInline(ConfigurableRelatedFieldWidgetMixin, admin.TabularInline):
            ...
            INLINE_RELATED_CONFIG = {
                'my_field': {
                    'can_add_related': False,
                },
            }
            ...
    """

    INLINE_RELATED_CONFIG = None

    def validate_inline_related_config(self, formset):
        """
        Validate that all fields in INLINE_RELATED_CONFIG exist in the formset.
        """
        if self.INLINE_RELATED_CONFIG is None:
            raise ValueError("INLINE_RELATED_CONFIG is not set.")
        for field in self.INLINE_RELATED_CONFIG.keys():
            if field not in formset.form.base_fields:
                raise ValueError(f"Field '{field}' in INLINE_RELATED_CONFIG does not exist in the formset.")

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        self.validate_inline_related_config(formset)
        for field, config in self.INLINE_RELATED_CONFIG.items():
            formset.form.base_fields[field].widget.can_add_related = config.get('can_add_related', True)
            formset.form.base_fields[field].widget.can_change_related = config.get('can_change_related', True)
        return formset
