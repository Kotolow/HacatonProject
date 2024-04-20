from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from db_app.serializers import UserSerializer, TasksSerializer
from db_app.models import User, Tasks
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
