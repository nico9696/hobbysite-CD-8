from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

def article_list(request):
    if request.user.is_authenticated:
        other_articles = Article.objects.exclude(author=request.user.profile).filter(category__isnull=False)
        user_articles = Article.objects.filter(author=request.user.profile).filter(category__isnull=False)
    else:
        other_articles = Article.objects.filter(category__isnull=False)
        user_articles = []

    articles_by_category = {}
    for article in other_articles:
        if article.category:
            articles_by_category.setdefault(article.category, []).append(article)
        else:
            articles_by_category.setdefault('Uncategorized', []).append(article)

    context = {
        'category_list': ArticleCategory.objects.all(),
        'articles_by_category': articles_by_category,
        'user_articles': user_articles,
        'create_article_link': True,
    }
    return render(request, 'blog/article_list.html', context)


def article_details(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.author = request.user.profile
            except AttributeError:
                return HttpResponseForbidden("User profile missing.")
            comment.article = article
            comment.save()
            return redirect('article_details', pk=article.pk)
    else:
        form = CommentForm()

    context = {
        'article': article,
        'related_articles': Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2],
        'comments': Comment.objects.filter(article=article).order_by('-created_on'),
        'comment_form': form,
    }
    return render(request, 'blog/article_details.html', context)


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            try:
                article.author = request.user.profile
            except AttributeError:
                return HttpResponseForbidden("User profile missing.")
            article.created_on = article.updated_on = timezone.now()
            article.save()
            return redirect('article_details', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})


@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    try:
        if request.user.profile != article.author:
            return HttpResponseForbidden()
    except AttributeError:
        return HttpResponseForbidden("User profile missing.")

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.updated_on = timezone.now()
            article.save()
            return redirect('article_details', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/article_update.html', {'form': form, 'article': article})
