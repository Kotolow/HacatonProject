from django.urls import include, path

from rest_framework.routers import DefaultRouter
from .views import EventView

router = DefaultRouter()

# router.register('events', EventView, basename='events')

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api/v1/events/', EventView.as_view(), name='events'),
]

