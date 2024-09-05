from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import (
    TemplateView, FormView, CreateView
)

from .form import UserLoginForm, UserRegisterForm
from .models import User


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


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            login(self.request, user)
            return redirect('index')

        else:
            return redirect('register')

        return super().form_valid(form)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = "/"


class PostView(TemplateView):
    template_name = "post.html"