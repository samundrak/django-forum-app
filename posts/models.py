from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
