from django.urls import path
from . import views

urlpatterns = [
    path('threads/', views.forum_list, name='forum_list'),
    path('thread/<int:forum_id>/', views.forum_detail, name='forum_detail'),
]