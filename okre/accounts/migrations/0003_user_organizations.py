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

# Generated by Django 5.2 on 2025-04-29 13:05

from django.db import migrations, models


def extract_username(user):
    """
    Return the username of the user.
    Implemented to return the part of the email before the '@' symbol.
    """
    return user.email.split('@')[0]

def create_organizations_for_existing_users(apps, schema_editor):
    """
    Create a default personal organization for existing users.
    This function is called during the migration to ensure that all existing users
    have at least one organization.
    """
    User = apps.get_model('accounts', 'User')
    Team = apps.get_model('organization', 'Team')

    for user in User.objects.all():
        if user.organizations.count() > 0:
            continue

        username = extract_username(user)
        if not username:
            print(f"User {user.pk} does not have a username. Skipping organization creation.")
            continue

        # Create the personal organization
        organization = Team.objects.create(
            name=f"{username}'s Personal Organization",
            is_organization=True,
        )
        user.organizations.add(organization)
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(
                blank=True,
                help_text='The organizations this user is a member of.',
                related_name='members',
                to='organization.team',
            ),
        ),
        migrations.RunPython(create_organizations_for_existing_users),
    ]
