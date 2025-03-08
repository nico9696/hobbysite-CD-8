from django.urls import path
from . import views

urlpatterns = [
    path('wiki/articles/', views.article_list, name='article_list'),
    path('wiki/article/<int:article_id>/', views.article_detail, name='article_detail'),
]
