from django.urls import path, include
from .views import (
    ArticleReadAPIView,
    ArticleAuthorAPIView,
    ArticleEditAPIView,
    ArticleAdminAPIView,
)

app_name = "articles"

urlpatterns = []
