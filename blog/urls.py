from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', views.article_list, name="blog_list"),
    path('article/<int:pk>/', views.article_details, name="article_details"),
    path('article/add/', views.article_create, name="article_create"),
    path('article/<int:pk>/edit/', views.article_update, name="article_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
