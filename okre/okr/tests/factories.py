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

from okr.models import Objective, KeyResult

class OrganizationObjectiveFactory(DjangoModelFactory):
    class Meta:
        model = Objective

    title = factory.Sequence(
        lambda n: f"Objective {n}"
    )
    description = factory.Faker("text", max_nb_chars=200)
    team = factory.SubFactory("organization.tests.factories.OrganizationFactory")


class TeamObjectiveFactory(DjangoModelFactory):
    class Meta:
        model = Objective

    title = factory.Sequence(
        lambda n: f"Objective {n}"
    )
    description = factory.Faker("text", max_nb_chars=200)
    team = factory.SubFactory("organization.tests.factories.TeamFactory")


class KeyResultFactory(DjangoModelFactory):
    class Meta:
        model = KeyResult

    title = factory.Sequence(
        lambda n: f"Key Result {n}"
    )
    description = factory.Faker("text", max_nb_chars=200)
    target_value = factory.Faker("random_int", min=0, max=100)
    current_value = factory.Faker("random_int", min=0, max=100)
    objective = factory.SubFactory(OrganizationObjectiveFactory)
