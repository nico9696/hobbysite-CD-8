from django.urls import path
#from . import views
from .views import article_list

urlpatterns = [
    ##path('articles/', views.article_list, name='article_list'),
    path('articles/', article_list.as_view(), name="article_list")
]
