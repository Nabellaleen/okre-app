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
