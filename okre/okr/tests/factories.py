import factory

from factory.django import DjangoModelFactory

from okr.models import Objective

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