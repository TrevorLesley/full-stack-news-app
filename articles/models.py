from django.conf import settings
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    category = models.CharField(max_length=255)
    published = models.BooleanField(verbose_name=("Verified"), default=False)
