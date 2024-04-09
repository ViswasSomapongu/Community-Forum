from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)    