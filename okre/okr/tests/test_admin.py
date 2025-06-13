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

from django.urls import reverse
from django.contrib.admin.sites import site
from django.urls.exceptions import NoReverseMatch

from okr.models import KeyResult

from .factories import OrganizationObjectiveFactory, KeyResultFactory


@pytest.mark.django_db
def test_keyresult_inline_in_objective_admin(client, admin_user):
    client.force_login(admin_user)
    objective = OrganizationObjectiveFactory()
    key_result = KeyResultFactory(title="KR Lorem", objective=objective)

    url = reverse("admin:okr_objective_change", args=[objective.pk])
    response = client.get(url)
    
    assert response.status_code == 200
    assert b"key_results-heading" in response.content
    assert key_result.title.encode() in response.content


def test_keyresult_not_registered_in_root_admin(client, admin_user):
    assert KeyResult not in site._registry
    with pytest.raises(NoReverseMatch):
        # This will raise an error, as okr_keyresult_change view is not registered
        fake_pk = 1
        reverse("admin:okr_keyresult_change", args=[fake_pk])
