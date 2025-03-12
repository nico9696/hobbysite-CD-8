from django.urls import path
#from . import views
from .views import ArticleList, ArticleDetails

urlpatterns = [
    ##path('articles/', views.article_list, name='article_list'),
    path('articles/', ArticleList.as_view(), name="article_list"),
    path('article/<int:pk>/', ArticleDetails.as_view(), name="article_details"),
]