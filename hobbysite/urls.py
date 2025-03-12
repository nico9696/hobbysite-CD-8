from django.urls import path
from . import views

urlpatterns = [
    path('commissions/', views.commission_list, name='commission_list'),
     path('commission/<int:commission_id>/', views.commission_detail, name='commission_detail'),
]