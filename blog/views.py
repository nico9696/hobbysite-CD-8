from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            try:
                return Article.objects.exclude(author=self.request.user.profile).filter(category__isnull=False)
            except AttributeError:
                return Article.objects.filter(category__isnull=False)
        return Article.objects.filter(category__isnull=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                context['user_articles'] = Article.objects.filter(author=self.request.user.profile)
            except AttributeError:
                context['user_articles'] = []
        context['category_list'] = self.get_queryset().order_by('category__name')
        return context

class ArticleDetails(DetailView):
    model = Article
    template_name = 'blog/article_details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['related_articles'] = Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2]
        context['comments'] = Comment.objects.filter(article=article).order_by('-created_on')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                comment.author = request.user.profile
            except AttributeError:
                return HttpResponseForbidden("User profile missing.")
            comment.article = self.object
            comment.save()
            return redirect('article_details', pk=self.object.pk)

        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user.profile
        except AttributeError:
            return HttpResponseForbidden("User profile missing.")
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'blog/article_update.html'
    form_class = ArticleForm

    def test_func(self):
        article = self.get_object()
        try:
            return self.request.user.profile == article.author
        except AttributeError:
            return False