from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_articles = Article.objects.filter(author__user=self.request.user)
            all_articles = Article.objects.exclude(author__user=self.request.user)
        else:
            user_articles = Article.objects.none()
            all_articles = Article.objects.all()
        return {
            'user_articles': user_articles,
            'grouped_articles': ArticleCategory.objects.prefetch_related('article_set'),
            'all_articles': all_articles
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querysets = self.get_queryset()
        context['user_articles'] = querysets['user_articles']
        context['grouped_articles'] = querysets['grouped_articles']
        context['all_articles'] = querysets['all_articles']
        return context

class ArticleDetails(DetailView):
    model = Article 
    template_name = 'blog/article_details.html'
    context_object_name = 'article'