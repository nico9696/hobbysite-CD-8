from django.urls import path
from commissions import views

urlpatterns = [
    path('list/', views.commission_list, name='commission_list'),
    path('detail/<int:commission_id>/', views.commission_detail, name='commission_detail'),
    path('add/', views.commission_create, name='commission_create'),
    path('edit/<int:commission_id>/', views.commission_update, name='commission_update'),
    path('commissions/job/create/<int:commission_id>/', views.job_detail, name='job_detail'),

]