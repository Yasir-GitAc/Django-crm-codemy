from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Task(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now= True)

  def __str__(self):
    return self.title
  
  # def get_absolute_url(self):
  #   return reverse(
  #     "home",
  #     kwargs={
  #         # "username": self.user.username,
  #         "pk": self.pk
  #     }
  #   )