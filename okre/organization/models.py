from django.db import models


class Team(models.Model):
    """
    Represents a group of users working together.
    It can be an organization, or a team within an organization.
    """
    name = models.CharField(max_length=255)
    is_organization = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE, # TODO: Handle the deletion of sub-teams when a parent team is deleted
        related_name='teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name
