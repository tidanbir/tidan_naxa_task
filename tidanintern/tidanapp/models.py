from ast import mod
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="userprofile")
    role = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.full_name 

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="task")
    task_name = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    

class Attendence(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="atendence")
    is_present = models.BooleanField(default=False)

