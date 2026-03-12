"""
URL routes for the news API.
Connects API endpoints to the view.
"""

from django.urls import path
from .views import *

urlpatterns = [
path('api/articles/', ArticleList.as_view()),
path('api/articles/<int:pk>/', ArticleDetail.as_view()),
path('api/articles/create/', ArticleCreate.as_view()),
path('api/articles/update/<int:pk>/', ArticleUpdate.as_view()),
path('api/articles/delete/<int:pk>/', ArticleDelete.as_view()),

path('api/articles/approved/', ApprovedArticlesList.as_view()),

path('api/newsletters/', NewsletterList.as_view()),
path('api/newsletters/create/', NewsletterCreate.as_view()),
]
