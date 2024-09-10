from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import (
    TemplateView, FormView,
    CreateView, UpdateView,
    DeleteView, DetailView,
    ListView
)

from .form import UserLoginForm, UserRegisterForm
from .models import User, Post


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class BlogView(ListView):
    template_name = "blog.html"
    model = Post
    context_object_name = "blogs"


class ContactView(TemplateView):
    template_name = "contact.html"


class BlogDetailView(TemplateView):
    template_name = "blog_detail.html"
