from rest_framework import serializers

from .models import Article


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ("title", "body", "author", "category")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ("title", "body", "author", "category")
