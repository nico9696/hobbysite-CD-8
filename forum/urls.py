from django.urls import path
from . import views

urlpatterns = [
    path('forum/threads/', views.forum_list, name='forum_list'),
    path('forum/thread/<int:forum_id>/', views.forum_detail, name='forum_detail'),
]