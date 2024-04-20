from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TasksViewSet, set_task

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='events')
router.register(r'tasks', TasksViewSet, basename='tags')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/set_task/', set_task, name='set_task'),
]

