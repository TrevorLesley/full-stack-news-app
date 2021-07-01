from django.urls import path
from .views import (
    ArticleReadAPIView,
    ArticleAuthorAPIView,
    ArticleEditAPIView,
    ArticleAdminAPIView,
)

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", ArticleEditAPIView.as_view(), name="article_detail"),
    path("", ArticleReadAPIView.as_view(), name="article_window"),
    path(
        "author_homescreen/", ArticleAuthorAPIView.as_view(), name="author_homescreen"
    ),
    path("admin/<int:pk>/", ArticleAdminAPIView.as_view(), name="admin_homescreen"),
]
