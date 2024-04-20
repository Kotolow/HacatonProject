import logging
import random

from db_app.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class TagsView(APIView):
    def get(self, request):
        tags = requests.get('https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories')
        queryset = tags.json()['data']
        return Response(queryset)


class EventView(APIView):

    def get(self, request, format=None):
        event_id = request.query_params.get('id')
        lat = request.query_params.get('lat')
        lng = request.query_params.get('lng')
        categories = {request.query_params.get('categories')}
        categories = {
            1: 'party',
            2: 'concert',
            3: 'walk',
            4: 'exhibition',
            5: 'kids',
            6: 'cinema',
            7: 'education',
            8: 'entertainment',
            9: 'fashion',
            10: 'holiday',
        }

        url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/events'

        params = {
            'lat': 59.939016,
            'lng': 30.31588,
            'radius': 10,
            'categories': {categories.get(random.randint(1, 10))},
            'fields': 'categories,description,id,place,title,age_restriction,is_free,images',
            'expand': 'images,place,location,dates,participants',
            'page': 1,
            'count': 10,
            'id': event_id
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            event_data = response.json()['data']
            return Response(event_data)
        else:
            return Response(status=response.status_code)
