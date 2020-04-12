import pytest
from django.urls import resolve, reverse

from {{ cookiecutter.project_slug }}.users.models import User

pytestmark = pytest.mark.django_db

def test_user_list():
    assert (
        reverse("user-list")
        == "/api/users/"
    )
    assert resolve("/api/users/").view_name == "user-list"


def test_user_me():
    assert reverse("user-me") == "/api/users/me/"
    assert resolve("/api/users/me/").view_name == "user-me"


def test_user_detail(user: User):
    assert (
        reverse("user-detail", kwargs={"username": user.username})
        == f"/api/users/{user.username}/"
    )
    assert resolve(f"/api/users/{user.username}/").view_name == "user-detail"
