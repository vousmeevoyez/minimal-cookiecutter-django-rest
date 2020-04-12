import pytest

from {{ cookiecutter.project_slug }}.users.models import User

pytestmark = pytest.mark.django_db


def test_user_models(user: User):
    assert user.name
