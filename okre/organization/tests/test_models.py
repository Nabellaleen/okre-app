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

import pytest

from .factories import  OrganizationFactory, TeamFactory

@pytest.mark.django_db
def test_team_can_be_organization():
    organization = OrganizationFactory()

    assert organization.is_organization is True
    assert organization.parent is None
    assert organization.members.count() == 0
    assert organization.name.startswith("Organization")
    assert organization.teams.count() == 0

    team = TeamFactory(parent=organization)
    assert team.is_organization is False
    assert team.parent == organization
    assert team.name.startswith("Team")
    assert team.members.count() == 0
    assert team.teams.count() == 0
