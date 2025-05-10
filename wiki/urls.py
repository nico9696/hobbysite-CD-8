from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "wiki"

urlpatterns = [
    path("", lambda request: redirect("wiki:wiki_list", permanent=False)),  # Redirect to 'wiki_list'
    path('articles/', views.article_list, name='wiki_list'), # Name written like this so that it does not clash with blog app's
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/add/', views.article_add, name='article_add'),
    path('article/<int:article_id>/edit/', views.article_edit, name='article_edit'),
]
