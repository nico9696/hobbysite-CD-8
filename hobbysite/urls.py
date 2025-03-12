from django.urls import path
from commission import views

urlpatterns = [
    path('commissions/list/', views.commission_list, name='commission_list'),
    path('commission/detail/<int:commission_id>/', views.commission_detail, name='commission_detail'),
]