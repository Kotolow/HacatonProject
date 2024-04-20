import uuid
from django.db import models
from django.contrib.auth.models import User

class User(User):
    userid = models.AutoField(primary_key=True)
    telegram_user_name = models.CharField(max_length=200, default=None, null=True)
    tags = models.TextField(default='{}') #using slag
    group_id = models.IntegerField(default=0)

class Tasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    done = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=None, null=True)
    end_time = models.DateTimeField(default=None, null=True)









