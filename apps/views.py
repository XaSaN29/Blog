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


class BlogView(TemplateView):
    template_name = "blog.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class SingleView(TemplateView):
    template_name = "single.html"


class PostView(TemplateView):
    template_name = "post.html"

