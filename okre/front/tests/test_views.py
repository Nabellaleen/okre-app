import pytest
import html

from django.urls import reverse
from django.utils.formats import localize

from accounts.tests.factories import UserFactory
from okr.tests.factories import KeyResultFactory
from organization.tests.factories import OrganizationFactory

@pytest.mark.django_db
def test_navigation_view(client):
    user = UserFactory()
    client.force_login(user)

    key_result = KeyResultFactory(objective__team=user.get_default_organization())

    objective = key_result.objective
    organization = objective.team
    
    url = reverse("front:navigation")
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()

    assert html.escape(organization.name) in content
    assert html.escape(user.get_username()) in content

    for objective in organization.objectives.all():
        assert objective.title in content

    for team in organization.teams.all():
        assert team.name in content
        for objective in team.objectives.all():
            assert objective.title in content

@pytest.mark.django_db
def test_objective_view(client):
    user = UserFactory()
    client.force_login(user)

    key_result = KeyResultFactory(objective__team=user.get_default_organization())
    objective = key_result.objective

    url = reverse("front:objective", args=[objective.id])
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()

    assert html.escape(objective.title) in content
    assert html.escape(objective.description) in content
    # assert html.escape(objective.team.name) in content

    advancement = objective.get_advancement()
    assert html.escape(localize(advancement['advancement'])) in content
    assert html.escape(localize(advancement['total_current'])) in content
    assert html.escape(localize(advancement['total_target'])) in content

    assert html.escape(key_result.title) in content
    assert html.escape(str(key_result.current_value)) in content
    assert html.escape(str(key_result.target_value)) in content
    assert html.escape(key_result.description) in content
