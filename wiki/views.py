from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ArticleCategory, Article
from .forms import ArticleForm


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
    article = Article.objects.get(id=article_id)
    related_articles = Article.objects.filter(category=article.category).exclude(id=article_id)[:2]

    ctx = {
        'article': article,
        'related_articles': related_articles
    }
    return render(request, 'wiki/article_detail.html', ctx)


@login_required
def article_add(request):
    # Check user's submitted information
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect('wiki_list')
    else:
        article_form = ArticleForm()

    return render(request, 'wiki/article_add.html', {'article_form': article_form})


def article_edit(request, article_id):
    ctx = {
        'article': Article.objects.get(id=article_id)
    }
    return render(request, 'wiki/article_edit.html', ctx)
