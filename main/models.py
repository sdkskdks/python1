from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField('name', max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
