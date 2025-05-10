from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('commissions/', include('commissions.urls'), name='commissions'),
    path('forum/', include('forum.urls'), name='forum'),
    path('blog/', include('blog.urls'), name='blog'),
    path('wiki/', include('wiki.urls'), name='wiki'),
    path('merchstore/', include('merchstore.urls'), name='merchstore'),
    path('profile/', include('user_management.urls'), name='user_management'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
