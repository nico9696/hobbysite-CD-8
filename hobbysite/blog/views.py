from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

#def article_list(request):
#    return render(request, 'blog/article_list.html', {})

class article_list(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_on']

