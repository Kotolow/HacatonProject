from rest_framework.serializers import ModelSerializer
from .models import Event, Tag


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['picked', 'name']
