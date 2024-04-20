from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import EventViewSet, TagViewSet

router = DefaultRouter()

router.register(r'events', EventViewSet, basename='events')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

