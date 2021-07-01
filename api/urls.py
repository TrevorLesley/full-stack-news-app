from django.urls import include, path

urlpatterns = [
    path("users/", include("accounts.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("articles/", include("articles.urls"), name="articles"),
]
