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

from .factories import UserFactory

@pytest.mark.django_db
def test_create_default_personal_organization():
    user = UserFactory()
    assert user.organizations.count() == 1

    personal_org = user.organizations.first()
    assert personal_org.name == f"{user.get_username()}'s Personal Organization"
    assert personal_org.is_organization is True
    assert personal_org.parent is None
    assert personal_org.members.count() == 1
    assert personal_org.members.first() == user
