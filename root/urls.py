"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from apps.views import IndexView, AboutView, LoginView, ProfilView, ProfilSettingsView, SearchView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('login/', LoginView.as_view(), name="login"),
    path('profil/', ProfilView.as_view(), name="profil"),
    path('profil-settings/', ProfilSettingsView.as_view(), name="profil-settings"),
    path('search/', SearchView.as_view(), name="search"),
    path('register/', RegisterView.as_view(), name="register")
]
