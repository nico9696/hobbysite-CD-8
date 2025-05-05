from django.shortcuts import render, redirect
from .models import ThreadCategory, Thread, Comment
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, CommentForm

def forum_list(request):
    user_threads = {}
    categories_with_threads = {}

    # threads created by user
    if request.user.is_authenticated:
        user_threads_qs = Thread.objects.filter(author=request.user.profile)
        user_threads = {thread.title: thread.id for thread in user_threads_qs}

    # threads by others (grouped by category)
    # loop through all category and get threads for each
    for category in ThreadCategory.objects.all():
        threads_in_category = Thread.objects.filter(category=category).exclude(author=request.user.profile if request.user.is_authenticated else None).order_by('title')

        unique_threads = {} # dictionary for unqiue thread titles within category
        for thread in threads_in_category:
            if thread.title not in unique_threads:
                unique_threads[thread.title] = thread.id

        categories_with_threads[category] = unique_threads

    ctx = {
        'user_threads': user_threads,
        'categories_with_threads': categories_with_threads
    }
    return render(request, 'forum/forum_list.html', ctx)

def forum_detail(request, forum_id):
    thread = Thread.objects.get(id=forum_id)
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

    related_threads = Thread.objects.filter(category=thread.category).exclude(id=thread.id)[:2]

    ctx = {
        'thread': thread,
        'comments': comments,
        'form': form,
        'related_threads': related_threads,
    }
    return render(request, 'forum/forum_detail.html', ctx)

@login_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            new_thread = form.save(commit=False)
            new_thread.author = request.user.profile
            new_thread.save()
            return redirect(new_thread.get_absolute_url())
    else:
        form = ThreadForm()

    return render(request, 'forum/thread_form.html', {'form': form})

@login_required
def thread_update(request, forum_id):
    thread = Thread.objects.get(id=forum_id)

    # Only allow to edit by thread author
    if thread.author != request.user.profile:
        return redirect('forum_detail', forum_id=forum_id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            return redirect(thread.get_absolute_url())
    else:
        form = ThreadForm(instance=thread)
        
    return render(request, 'forum/thread_form.html', {'form': form})