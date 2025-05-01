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
