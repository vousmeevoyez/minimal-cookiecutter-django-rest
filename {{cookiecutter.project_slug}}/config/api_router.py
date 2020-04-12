from {{ cookiecutter.project_slug }}.users.urls import urlpatterns as \
    users_url_patterns

app_name = "api"
urlpatterns = []
urlpatterns += [
    users_url_patterns
]
