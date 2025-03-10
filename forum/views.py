from django.shortcuts import render
from .models import PostCategory, Post

def forum_list(request):
    ctx = {
        'categories': PostCategory.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'forum_list.html', ctx)

def article_detail(request, forum_id):
    ctx = {
        'forum': Post.objects.get(id=forum_id)
    }
    return render(request, 'forum_detail.html', ctx)