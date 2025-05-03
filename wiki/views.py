from django.shortcuts import render
from .models import ArticleCategory, Article


def article_list(request):
    user = request.user

    # Separate user's articles from the rest of the list
    if user.is_authenticated:
        profile = user.profile
        ctx = {
            'user_articles': Article.objects.filter(author=profile),
            'non_user_articles': Article.objects.exclude(author=profile),
            'categories': ArticleCategory.objects.all()
        }
    else:
        ctx = {
            'user_articles': Article.objects.none(),
            'non_user_articles': Article.objects.all(),
            'categories': ArticleCategory.objects.all()
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
