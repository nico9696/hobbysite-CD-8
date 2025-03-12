from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_on']

    def get_queryset(self):
        return Article.objects.filter(category__isnull=False)

class ArticleDetails(DetailView):
    model = Article 
    template_name = 'blog/article_details.html'
    context_object_name = 'article'