from django.shortcuts import render
from .models import ArticleCategory, Article


def article_list(request):
    ctx = {
        'categories': ArticleCategory.objects.all(),
        'articles': Article.objects.all()
    }
    return render(request, 'wiki/article_list.html', ctx)


def article_detail(request, article_id):
    ctx = {
        'article': Article.objects.get(id=article_id)
    }
    return render(request, 'wiki/article_detail.html', ctx)


def article_add(request):
    return render(request, 'wiki/article_add.html')


def article_edit(request, article_id):
    ctx = {
        'article': Article.objects.get(id=article_id)
    }
    return render(request, 'wiki/article_edit.html', ctx)
