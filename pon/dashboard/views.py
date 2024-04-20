from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response


class TagViewSet(mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet, ):
    pass


class EventViewSet(ModelViewSet):
    pass

