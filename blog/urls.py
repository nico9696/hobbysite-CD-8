from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles/', ArticleList.as_view(), name="article_list"),
    path('article/<int:pk>/', ArticleDetails.as_view(), name="article_details"),
]