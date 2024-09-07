from django.contrib import admin
from .models import User, Post


# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ['username']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')