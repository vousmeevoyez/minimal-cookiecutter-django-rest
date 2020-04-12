import pytest
from django.urls import resolve, reverse

from {{ cookiecutter.project_slug }}.users.models import User


def test_user_list():
    assert (
        reverse("user-list")
        == f"/users/"
    )
    assert resolve(f"/users/").view_name == "users:list"


def test_user_me():
    assert reverse("user-me") == "/users/me/"
    assert resolve("/users/me/").view_name == "users:me"


def test_user_detail(user: User):
    assert (
        reverse("user-detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/users/{user.username}/").view_name == "users:detail"
