from django.core import paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
import requests


class EventPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EventView(APIView):
    pagination_class = EventPagination

    def get(self, request):
        events = requests.get(f'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/events'
                              '?lat=59.939016&'
                              'lng=30.31588&'
                              'radius=5&'
                              'categories=exhibition%2C-concert&'
                              'fields=categories%2C'
                              'description%2C'
                              'id%2C'
                              'place%2C'
                              'title%2C'
                              'age_restriction%2C'
                              'is_free%2C'
                              'images&expand=images%2C'
                              'place%2C'
                              'location%2C'
                              'dates%2C'
                              'participants&'
                              f'page=1&'
                              f'count=10')

        queryset = events.json()['data']

        return Response(queryset)
