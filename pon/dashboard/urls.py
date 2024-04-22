from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import EventView, TagsView

urlpatterns = [
    path('api/v1/events/', EventView.as_view(), name='events'),
    path('api/v1/tags/', TagsView.as_view(), name='event'),
]
