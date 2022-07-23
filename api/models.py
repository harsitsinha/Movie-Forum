from django.db import models

# Create your models here.

class Comment(models.Model):
    user_comment = models.TextField(default='')