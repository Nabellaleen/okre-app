import pytest

from .factories import OrganizationObjectiveFactory, TeamObjectiveFactory, KeyResultFactory

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

@pytest.mark.django_db
def test_key_result_creation():
    key_result = KeyResultFactory(target_value=80, current_value=50)
    assert key_result.title.startswith("Key Result")
    assert isinstance(key_result.description, str)
    assert key_result.target_value == 80
    assert key_result.current_value == 50
    assert str(key_result).endswith("(50/80)")

    assert key_result.objective is not None
    assert key_result.objective.title.startswith("Objective")

    assert key_result.objective.key_results.count() == 1
    assert key_result.objective.key_results.first() == key_result


@pytest.mark.django_db
def test_key_result_string_representation():
    key_result_1 = KeyResultFactory(title="Test Key Result", target_value=90, current_value=75)
    assert str(key_result_1) == "Test Key Result (75/90)"

    key_result_2 = KeyResultFactory(title="Another Key Result", target_value=100, current_value=50.5)
    assert str(key_result_2) == "Another Key Result (50.5/100)"

    key_result_3 = KeyResultFactory(title="Negative Key Result", target_value=-10, current_value=-5)
    assert str(key_result_3) == "Negative Key Result (-5/-10)"
