from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)


class Post(BaseModel):
    image = models.ImageField(upload_to='post/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title



