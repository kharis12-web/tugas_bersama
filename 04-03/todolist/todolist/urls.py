from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('task/', include('task.urls')),
    path('datakaryawan/', include('datakaryawan.urls')),
    
    path('', include('home.urls')),
]


