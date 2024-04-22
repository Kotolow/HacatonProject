from django.urls import path, include
from .views import UserRegistration

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/register/', UserRegistration.as_view(), name='register'),
]
