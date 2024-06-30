from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('quien', views.index2, name="index2"),
 	path('servicios', views.index3, name="index3"),
	
]