from django.shortcuts import render
from .models import PostCategory, Post

def forum_list(request):
    categories_with_threads = {}

    # loop through all category and get posts for each
    for category in PostCategory.objects.all():
        posts_in_category = Post.objects.filter(category=category).order_by('title')

        unique_threads = {} # dictionary for unqiue thread titles within category
        for post in posts_in_category:
            if post.title not in unique_threads:
                unique_threads[post.title] = post.id

        categories_with_threads[category] = unique_threads

    ctx = {
        'categories_with_threads': categories_with_threads
    }
    return render(request, 'forum/forum_list.html', ctx)

def forum_detail(request, forum_id):
    post = Post.objects.get(id=forum_id)

    ctx = {
        'thread_title': post.title,
        'posts': Post.objects.filter(title=post.title),
        'category': post.category
    }
    return render(request, 'forum/forum_detail.html', ctx)