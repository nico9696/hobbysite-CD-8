from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ArticleForm, CommentForm


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
    related_articles = Article.objects.filter(category=article.category).exclude(id=article_id)[:5]
    comments = Comment.objects.filter(article=article).order_by('-created_on')

    user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            wiki_comment = comment_form.save(commit=False)
            wiki_comment.author = request.user.profile
            wiki_comment.article = article
            wiki_comment.save()
            return redirect(article.get_absolute_url())
    else:
        comment_form = CommentForm()

    ctx = {
        'article': article,
        'related_articles': related_articles,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'wiki/article_detail.html', ctx)


@login_required
def article_add(request):
    # Check user's submitted information
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            wiki_article = article_form.save(commit=False)
            wiki_article.author = request.user.profile
            wiki_article.save()
            return redirect(wiki_article.get_absolute_url())
    else:
        article_form = ArticleForm()

    return render(request, 'wiki/article_add.html', {'article_form': article_form})


@login_required
def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect(article.get_absolute_url())
    else:
        article_form = ArticleForm(instance=article)

    ctx = {
        'article': article,
        'article_form': article_form
    }
    return render(request, 'wiki/article_edit.html', ctx)
