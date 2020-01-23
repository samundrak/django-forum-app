from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts


# Create your models here.
class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
