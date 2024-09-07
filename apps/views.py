from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import (
    TemplateView, FormView, CreateView, UpdateView, DeleteView, DetailView, ListView
)

from .form import UserLoginForm, UserRegisterForm
from .models import User, Post


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class PostView(ListView):
    template_name = "post.html"
    model = Post
    context_object_name = "posts"


class BlogView(TemplateView):
    template_name = "blog.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class SingleView(TemplateView):
    template_name = "single.html"


class PostView(TemplateView):
    template_name = "post.html"

