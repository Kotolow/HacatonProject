from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import EventSerializer, TagSerializer
from .models import Event, Tag
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response


class TagViewSet(mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet, ):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

