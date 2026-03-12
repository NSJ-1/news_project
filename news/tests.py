from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Publisher


class ArticleTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.publisher = Publisher.objects.create(name="BBC")

    def test_article_creation(self):
        article = Article.objects.create(
            title="Test Article",
            content="Test content",
            author=self.user,
            publisher=self.publisher,
            approved=True
        )

        self.assertEqual(article.title, "Test Article")
