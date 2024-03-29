from rest_framework import serializers
from .models import Issue, Author, Article, Category

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issue
        fields='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'