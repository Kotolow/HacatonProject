from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('jobs/', include('jobs.urls')),
    path('schedule/', include('schedule.urls')),
    path('db_app/', include('db_app.urls')),

]
