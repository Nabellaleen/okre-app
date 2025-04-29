from django.db.models.signals import post_save
from django.dispatch import receiver

from organization.models import Team

from .models import User

@receiver(post_save, sender=User)
def create_default_personal_organization(sender, instance, created, **kwargs):
    """
    Create a default personal organization for the user when the user is created.
    """
    if not created:
        return
    if instance.organizations.count() > 0:
        return

    username = instance.get_username()
    if not username:
        raise ValueError("User must have a username to create a personal organization.")
    
    # Create the personal organization
    organization = Team.objects.create(
        name=f"{username}'s Personal Organization",
        is_organization=True,
    )
    instance.organizations.add(organization)
