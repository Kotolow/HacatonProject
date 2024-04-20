from rest_framework.viewsets import ModelViewSet, GenericViewSet
from db_app.serializers import UserSerializer, TasksSerializer
from db_app.models import User, Tasks
from .helpers import TasksHelper
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TasksViewSet(ModelViewSet):
    helper = TasksHelper()
    helper.schedule_to_tasks(9370)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


@api_view(['POST'])
def set_task(request):
    serializer = TasksSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
