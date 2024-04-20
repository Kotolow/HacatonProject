from django.urls import path
from db_app.views import signup, login



urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
