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
