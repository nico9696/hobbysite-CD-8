from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/profile/home/')),  
    path('admin/', admin.site.urls),
    path('commissions/', include('commissions.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('wiki/', include('wiki.urls')),
    path('merchstore/', include('merchstore.urls')),
    path('profile/', include('user_management.urls')),
]
