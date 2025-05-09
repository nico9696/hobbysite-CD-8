from django.urls import path
from commissions import views

urlpatterns = [
    path('list/', views.commission_list, name='commission_list'),
    path('detail/<int:commission_id>/', views.commission_detail, name='commission_detail'),
    path('add/', views.commission_create, name='commission_create'),
    path('<int:commission_id>/edit/', views.commission_update, name='commission_update'),
    path('commissions/<int:commission_id>/job/create/', views.job_create, name='job_create'),
    path('job/<int:job_id>/applicants/', views.job_detail, name='job_detail'),
    path('commissions/<int:commission_id>/job/edit/', views.job_update, name='job_update'),
]