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
