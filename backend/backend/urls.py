from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/base-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('api/', include('main.urls', namespace='')),
    path('admin/', admin.site.urls),
]
