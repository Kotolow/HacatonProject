import logging
import random

from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class TagsView(APIView):
    def get(self, request):
        url = 'https://kudago.com/public-api/v1.4/event-categories/'
        tags = requests.get(url).json()
        queryset = []
        for item in tags:
            queryset.append(item['slug'])

        return Response(queryset)

    def post(self, request):
        selected_tags_slug = request.data.get('tags', [])
        user = request.user

        user.tags.clear()
        user.tags.add(*selected_tags_slug)

        return Response(status=200)


class EventView(APIView):

    def get(self, request, format=None):

        user = request.user
        categories = ','.join([str(tag.name) for tag in user.tags.all()])

        url = 'https://kudago.com/public-api/v1.4/events/'

        params = {
            'fields': 'categories,description,id,place,title,age_restriction,is_free,images,tags',
            'expand': 'images,place,location,dates,participants',
            'categories': ','.join([str(category.name) for category in categories]),
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            event_data = response.json()
            return Response(event_data)
        else:
            return Response(status=response.status_code)
