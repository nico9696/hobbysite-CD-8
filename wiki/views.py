from django.shortcuts import render, HttpResponse
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    ctx = {'articles': articles}
    return render(request, 'article_list.html', ctx)


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    ctx = {'article': article}
    return render(request, 'article_detail.html', ctx)
