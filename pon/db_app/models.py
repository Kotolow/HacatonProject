import uuid
from django.db import models
from django.contrib.auth.models import User

class User(User):
    userid = models.AutoField(primary_key=True)
    telegram_user_name = models.CharField(max_length=200, default=None)
    tags = models.TextField(default='{}') #using slag

class Tasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()









