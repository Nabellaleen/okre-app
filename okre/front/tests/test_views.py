import pytest

from django.urls import reverse

from okr.tests.factories import KeyResultFactory
from organization.tests.factories import OrganizationFactory

@pytest.mark.django_db
def test_navigation_view(client, admin_user):
    client.force_login(admin_user)
    organization = OrganizationFactory(name="Megacorp Inc.")
    key_result = KeyResultFactory(objective__team=organization)

    objective = key_result.objective
    organization = objective.team
    
    url = reverse("front:navigation")
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode()

    assert organization.name in content
    assert admin_user.get_username() in content

    # for objective in organization.objectives.all():
    #     assert objective.title in content

    # for team in organization.teams.all():
    #     assert team.name in content
    #     for objective in team.objectives.all():
    #         assert objective.title in content

