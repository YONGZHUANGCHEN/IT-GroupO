from django.contrib import admin
from django.urls import path
from django.urls import include
from CPUNerd import views


"""CPUNerd_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('social/', include('social_django.urls', namespace='social')),  # social login
    path('', views.index, name='index'),
    path('cpunerd/', include('CPUNerd.urls', namespace='CPUNerd')),
    path('user-profile/', include('user_profile.urls', namespace='user_profile')),
    #开头为cpunerd/的所有urls都会自动进行匹配
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^static/(?P<path>.*)$', serve,  {'document_root': settings.STATIC_ROOT}, name='static'),
    ]