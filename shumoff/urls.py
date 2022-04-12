"""shumoff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('shumoffcenter-administrator-panel/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('account/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # local apps
    path('', include('core.urls', namespace='Core')),
    path('Home/', include('main.urls', namespace='Main')),
    path('accounts/', include('users.urls', namespace='User')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)