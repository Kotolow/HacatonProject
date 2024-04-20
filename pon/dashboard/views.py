from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer
from .models import Event, Tag


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

