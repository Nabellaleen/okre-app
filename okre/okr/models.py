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
