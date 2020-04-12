from django.urls import include, path

from rest_framework.routers import SimpleRouter
from {{ cookiecutter.project_slug }}.users.views import UserViewSet

router = SimpleRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]
