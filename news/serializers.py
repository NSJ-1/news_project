"""
Serializers for the news app.
Convert models to JSON for the API.
"""

from rest_framework import serializers
from .models import Article, Newsletter, Publisher, User


class ArticleSerializer(serializers.ModelSerializer):
    """Serliazer for article data."""
    class Meta:
        model = Article
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    """Serializer for newsletters."""
    class Meta:
        model = Newsletter
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """Serializer for publishers."""
    class Meta:
        model = Publisher
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users."""
    class Meta:
        model = User
        fields = '__all__'
