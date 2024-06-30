from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('quien', views.index2, name="index2"),
 	path('servicios', views.index3, name="index3"),
	path('nombreCompleto', views.staff1, name="index2"),
	path('soy', views.staff1, name="index2"),
	path('cargo', views.staff1, name="index2")
]