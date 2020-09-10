from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('task/', include('task.urls')),
    path('suplayer/', include('suplayer.urls')),
    path('alat/', include('alat.urls')),
    path('stokkopi/', include('alat.urls')),
    path('', include('home.urls')),
]


