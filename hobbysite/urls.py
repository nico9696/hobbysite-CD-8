from django.contrib import admin
from django.urls import path
from commissions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commissions/list/', views.commission_list, name='commission_list'),
    path('commissions/detail/<int:commission_id>/', views.commission_detail, name='commission_detail'),
]