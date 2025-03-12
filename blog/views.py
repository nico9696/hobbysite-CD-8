from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

#def article_list(request):
#    return render(request, 'blog/article_list.html', {})

class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_on']

class ArticleDetails(DetailView):
    model = Article 
    template_name = 'blog/article_details.html'
    context_object_name = 'article'