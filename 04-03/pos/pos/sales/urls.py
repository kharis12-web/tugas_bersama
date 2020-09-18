from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('input/', views.input),
	path('print/', views.print),
	path('<id>/delete', views.delete),
	path('<id>/update', views.update),
]