from .models import User, Tasks
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
