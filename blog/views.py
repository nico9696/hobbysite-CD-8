from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_articles = Article.objects.filter(author__user=self.request.user)
            all_articles = Article.objects.exclude(author__user=self.request.user)
        else:
            user_articles = Article.objects.none()
            all_articles = Article.objects.all()
        return {
            'user_articles': user_articles,
            'grouped_articles': ArticleCategory.objects.prefetch_related('article_set'),
            'all_articles': all_articles
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querysets = self.get_queryset()
        context['user_articles'] = querysets['user_articles']
        context['grouped_articles'] = querysets['grouped_articles']
        context['all_articles'] = querysets['all_articles']
        return context

class ArticleDetails(DetailView):
    model = Article
    template_name = 'blog/article_details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        context['related_articles'] = Article.objects.filter(author=article.author).exclude(pk=article.pk)[:2]
        context['comments'] = Comment.objects.filter(article=article).order_by('-created_on')
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user.profile
                comment.article = self.object
                comment.save()
        return redirect('article_details', pk=self.object.pk)

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
