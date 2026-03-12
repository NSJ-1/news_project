"""
Models for the news application.
Defines publishers, articles and newsletters.
"""

from django.db import models
from django.contrib.auth.models import User

class Publisher(models.Model):
    """Stores publisher information."""
    name = models.CharField(max_length=200)

class Article(models.Model):
    """Represents a news article."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Newsletter(models.Model):
    """Newsletter containing articles for subscribers."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)
    subscribers = models.ManyToManyField(User, related_name="subscriptions", blank=True)
