from rest_framework.viewsets import ModelViewSet, GenericViewSet
from db_app.serializers import UserSerializer, TasksSerializer
from db_app.models import User, Tasks
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.functions import TruncDay
from collections import defaultdict
from django.db.models import Q
import datetime


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


@api_view(['POST'])
def set_task(request):
    serializer = TasksSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_calendar(request):
    print(request.query_params)
    month = request.query_params.get('month')
    year = request.query_params.get('year')

    if month is None or year is None:
        return Response({'error': 'Month and year parameters are required.'}, status=400)

    try:
        month = int(month)
        year = int(year)

        datetime.datetime(year=year, month=month, day=1)
    except ValueError as e:
        return Response({'error': str(e)}, status=400)

    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
    queryset = Tasks.objects.filter(
        Q(start_time__gte=start_date) & Q(start_time__lt=end_date)
    ).annotate(day=TruncDay('start_time')).order_by('day')

    tasks_by_day = defaultdict(list)
    for task in queryset:
        tasks_by_day[task.day.strftime('%Y-%m-%d')].append({
            'taskid': task.taskid,
            'name': task.name,
            'description': task.description,
            'done': task.done,
            'start_time': task.start_time,
            'end_time': task.end_time
        })

    return Response(tasks_by_day)
