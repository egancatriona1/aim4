"""aim4 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from aim4.users.views import home, profile
from aim4.challenges.views import challenges, challenge_detail, challenge_join, challenge_refresh

urlpatterns = [

    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('challenges/', challenges, name='challenges',),

    url(r'^challenges/(?P<challenge_id>\d+)$', challenge_detail, name='challenge_detail'),
    url(r'^challenges/(?P<challenge_id>\d+)/join$', challenge_join, name='challenge_join'),
    url(r'^challenges/(?P<challenge_id>\d+)/refresh$', challenge_refresh, name='challenge_refresh'),


    path('profile', profile, name='profile'),

    path('privacy_policy/', TemplateView.as_view(template_name='corp/privacy_policy.html')),
    path('terms_of_service/', TemplateView.as_view(template_name='corp/terms_of_service.html')),

    url(r'', include('webmaster_verification.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

