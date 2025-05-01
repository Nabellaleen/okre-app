import pytest

from .factories import UserFactory

@pytest.mark.django_db
def test_create_default_personal_organization():
    user = UserFactory()
    assert user.organizations.count() == 1

    personal_org = user.organizations.first()
    assert personal_org.name == f"{user.get_username()}'s Personal Organization"
    assert personal_org.is_organization is True
    assert personal_org.parent is None
    assert personal_org.members.count() == 1
    assert personal_org.members.first() == user
