from django.shortcuts import render, redirect
from .models import ThreadCategory, Thread, Comment
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, CommentForm, ThreadCategoryForm

def forum_list(request):
    user_threads_by_category = {}
    other_threads_by_category = {}

    if request.user.is_authenticated:
        profile = request.user.profile

        # loop through all category, filter (by user or other), and get threads for each
        for category in ThreadCategory.objects.all():
            user_threads = Thread.objects.filter(author=profile, category=category).order_by('title')
            other_threads = Thread.objects.filter(category=category).exclude(author=profile).order_by('title')

            user_threads_by_category[category] = {t.title: t.id for t in user_threads}
            other_threads_by_category[category] = {t.title: t.id for t in other_threads}
    else:
        for category in ThreadCategory.objects.all():
            other_threads = Thread.objects.filter(category=category).order_by('title')
            other_threads_by_category[category] = {t.title: t.id for t in other_threads}

    ctx = {
        'user_threads_by_category': user_threads_by_category,
        'other_threads_by_category': other_threads_by_category,
    }
    return render(request, 'forum/forum_list.html', ctx)

def forum_detail(request, forum_id):
    thread = Thread.objects.get(id=forum_id)
    related_threads = Thread.objects.filter(category=thread.category).exclude(id=thread.id)[:3]
    comments = Comment.objects.filter(thread=thread)

    # Handle CommentForm
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.thread = thread
            new_comment.author = request.user.profile
            new_comment.save()
            return redirect('forum_detail', forum_id=forum_id)
    else:
        form = CommentForm()

    ctx = {
        'thread': thread,
        'related_threads': related_threads,
        'comments': comments,
        'form': form,
    }
    return render(request, 'forum/forum_detail.html', ctx)

@login_required
def thread_create(request):

    if request.method == 'POST':
        if 'add_thread' in request.POST:
            form = ThreadForm(request.POST, request.FILES)
            if form.is_valid():
                new_thread = form.save(commit=False)
                new_thread.author = request.user.profile
                new_thread.save()
                return redirect('forum_detail', forum_id=new_thread.id)
        elif 'add_category' in request.POST:
            category_form = ThreadCategoryForm(request.POST)
            if category_form.is_valid():
                new_category = category_form.save()
                return redirect('forum_list')
    else:
        form = ThreadForm()
        category_form = ThreadCategoryForm()
    
    ctx = {
        'form': form,
        'category_form': category_form,
    }
    return render(request, 'forum/thread_create.html', ctx)

@login_required
def thread_update(request, forum_id):
    thread = Thread.objects.get(id=forum_id)

    # Only allow to edit by thread author
    if thread.author != request.user.profile:
        return redirect('forum_detail', forum_id=thread.id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('forum_detail', forum_id=thread.id)
    else:
        form = ThreadForm(instance=thread)
        
    ctx = {
        'form': form,
        'thread': thread,
    }
    return render(request, 'forum/thread_update.html', ctx)