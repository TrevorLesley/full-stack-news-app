from rest_framework import generics
from .models import Article
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .permissions import IsAuthOrReadOnly
from .serializers import ArticleSerializer

# Create your views here.


class ArticleReadAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = (IsAuthenticatedOrReadOnly,)


class ArticleAuthorAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = (IsAuthOrReadOnly,)


class ArticleEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = (IsAuthOrReadOnly,)


class ArticleAdminAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = IsAdminUser
