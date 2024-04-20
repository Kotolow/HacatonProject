from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class EventView(APIView):
    def get(self, request):
        events = requests.get('https://spb-afisha.gate.petersburg.ru/kg/external/afisha/events')
        queryset = events.json()['data']
        return Response(queryset)
