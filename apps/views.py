from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ProfilView(TemplateView):
    template_name = "profil.html"


class SearchView(TemplateView):
    template_name = "sarch.html"


class ProfilSettingsView(TemplateView):
    template_name = "profil-settings.html"


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterView(TemplateView):
    template_name = "register.html"