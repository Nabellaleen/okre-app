from django.db import models

class Objective(models.Model):
    """
    Model to represent objectives.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    team = models.ForeignKey(
        'organization.Team',
        on_delete=models.CASCADE,
        related_name='objectives',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class KeyResult(models.Model):
    """
    Model to represent key results associated with objectives.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target_value = models.FloatField()
    current_value = models.FloatField()
    objective = models.ForeignKey(
        Objective,
        on_delete=models.CASCADE,
        related_name='key_results',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.current_value}/{self.target_value})"
