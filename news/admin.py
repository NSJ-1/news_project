from django.contrib import admin
from .models import Article, Publisher, Newsletter

admin.site.register(Article)
admin.site.register(Publisher)
admin.site.register(Newsletter)
