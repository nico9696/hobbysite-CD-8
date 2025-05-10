from django.urls import path
from . import views
from django.shortcuts import redirect

app_name = "forum"

urlpatterns = [
    path("", lambda request: redirect("forum:forum_list", permanent=False)),  # Redirect to 'forum_list'
    path('threads/', views.forum_list, name='forum_list'),
    path('thread/<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('thread/add/', views.thread_create, name='thread_create'),
    path('thread/<int:forum_id>/edit/', views.thread_update, name='thread_update'),
]