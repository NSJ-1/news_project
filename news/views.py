"""
Views for the news API.
Handles articles and newsletters.
"""

from rest_framework import generics
from .models import Article, Newsletter
from .serializers import ArticleSerializer, NewsletterSerializer


class ArticleList(generics.ListAPIView):
    """Shows all approved articles."""
    queryset = Article.objects.filter(approved=True)
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    """Returns a single article by id."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreate(generics.CreateAPIView):
    """Allows journalists to create articles."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name="Journalist").exists():
            serializer.save(author=self.request.user)


class ArticleUpdate(generics.UpdateAPIView):
    """Allows editors to update articles."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_update(self, serializer):
        if self.request.user.groups.filter(name="Editor").exists():
            serializer.save()


class ArticleDelete(generics.DestroyAPIView):
    """Allows deletion of articles."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class NewsletterList(generics.ListAPIView):
    """Shows a list of newsletters."""
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewsletterCreate(generics.CreateAPIView):
    """Creates a new newsletter."""
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

"""
Returns only approved articles.
"""
class ApprovedArticlesList(generics.ListAPIView):
    queryset = Article.objects.filter(approved=True)
    serializer_class = ArticleSerializer
