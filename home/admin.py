from django.contrib import admin
from .models import navbarmenu, staff, portafolio, servicio, Genero, Alumno


# Register your models here.

admin.site.register(navbarmenu)
admin.site.register(staff)
admin.site.register(portafolio)
admin.site.register(servicio)
admin.site.register(Genero)
admin.site.register(Alumno)