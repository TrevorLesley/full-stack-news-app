from rest_framework import generics
from .models import Article

from .permissions import IsAuthOrReadOnly
from .serializers import ArticleSerializer

# Create your views here.


class ArticleReadAPIView(generics.ListAPIView):
    queryset = get.objects.filter()
