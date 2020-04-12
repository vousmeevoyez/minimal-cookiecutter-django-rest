from django.urls import include, path

# API URLS
urlpatterns = [
    # API base url
    path("api/", include("config.api_router")),
]
