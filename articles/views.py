from rest_framework import generics
from .models import Article
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .permissions import IsAuthOrReadOnly
from .serializers import UserSerializer, AuthorSerializer, AdminSerializer

# Create your views here.


class ArticleReadAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = UserSerializer


class ArticleAuthorAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = UserSerializer
    permissions_classes = (IsAuthOrReadOnly,)


class ArticleEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(author=user)

    serializer_class = AuthorSerializer
    permissions_classes = (IsAuthOrReadOnly,)


class ArticleAdminAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = AdminSerializer
    permissions_classes = IsAdminUser
