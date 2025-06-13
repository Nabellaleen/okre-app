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
