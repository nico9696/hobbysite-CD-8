from django.urls import path
from .views import ArticleList, ArticleDetails, ArticleCreate, ArticleUpdate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', ArticleList.as_view(), name="blog_list"),
    path('article/<int:pk>/', ArticleDetails.as_view(), name="article_details"),
    path('article/add/', ArticleCreate.as_view(), name="article_create"),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name="article_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)