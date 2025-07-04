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

import factory
from factory.django import DjangoModelFactory

from organization.models import Team


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Sequence(
        lambda n: f"Organization {n}"
    )
    is_organization = True
    parent = None
    

class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Sequence(
        lambda n: f"Team {n}"
    )
    is_organization = False
    parent = factory.SubFactory(OrganizationFactory)
