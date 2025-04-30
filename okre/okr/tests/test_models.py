import pytest

from .factories import OrganizationObjectiveFactory, TeamObjectiveFactory

@pytest.mark.django_db
def test_organization_objective_creation():
    """
    Test the creation of an Objective instance.
    """

    objective = OrganizationObjectiveFactory()

    assert objective.title.startswith("Objective")
    assert isinstance(objective.description, str)
    assert objective.team.name.startswith("Organization")
    assert objective.team.is_organization is True


@pytest.mark.django_db
def test_team_objective_creation():
    """
    Test the creation of an Objective instance with a team.
    """

    objective = TeamObjectiveFactory()

    assert objective.title.startswith("Objective")
    assert isinstance(objective.description, str)
    assert objective.team.name.startswith("Team")
    assert objective.team.is_organization is False
    assert objective.team.parent.name.startswith("Organization")
    assert objective.team.parent.is_organization is True
