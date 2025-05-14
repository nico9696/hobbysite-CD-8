from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commissions/', include('commissions.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('wiki/', include('wiki.urls')),
    path('merchstore/', include('merchstore.urls')),
    path('profile/', include('user_management.urls')),
    path('', RedirectView.as_view(url='/profile/login/', permanent=False)),  # Redirect root URL to profile/login/
]