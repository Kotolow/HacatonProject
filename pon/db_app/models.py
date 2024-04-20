import uuid
from django.db import models
from django.contrib.auth.models import User

class User(User):
    userid = models.AutoField(primary_key=True)
    telegram_user_name = models.CharField(max_length=200)
    tags = models.CharField(max_length=2000) #using slag







