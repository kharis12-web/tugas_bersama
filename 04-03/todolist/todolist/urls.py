from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('buy/', include('buy.urls')),
    path('task/', include('task.urls')),
    path('suplayer/', include('suplayer.urls')),
    path('alat/', include('alat.urls')),
    path('stokkopi/', include('alat.urls')),
    path('datakaryawan/', include('datakaryawan.urls')),
    path('', include('home.urls')),
]


