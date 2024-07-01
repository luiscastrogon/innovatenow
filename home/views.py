from django.shortcuts import render
from .models import navbarmenu
from .models import staff
from .models import Alumno
from .models import Genero
from .models import servicio

# Create your views here.

def index(request):
	navbarmenus = navbarmenu.objects.all()
	context = { "navbarmenus": navbarmenus }	
	return render (request, 'home/index.html', context)

def index2(request):
	navbarmenus = navbarmenu.objects.all()
	staffs = staff.objects.all()
	context = { 
        "navbarmenus": navbarmenus,
        "staffs": staffs    
    }	
	return render (request, 'quien/index2.html', context)

def index3(request):
	navbarmenus = navbarmenu.objects.all()
	servicios = servicio.objects.all()
	context = { 
        "navbarmenus": navbarmenus,
        "servicios": servicios
    }	
	return render (request, 'servicios/index3.html', context)

def alumnosAdd(request):
	if request.method is not "POST":
		generos = Genero.objects.all()
		context={'generos':generos}
		return render(request, 'home/alumnos_add.html', context)
	else:	
		rut=request.post["rut"]
		nombre=request.post["nombre"]
		aPaterno=request.post["paterno"]
		aMaterno=request.post["materno"]
		fechanac=request.post["fechaNac"]
		genero=request.post["genero"]
		telefono=request.post["telefono"]
		email=request.post["email"]
			
		objGenero=Genero.objects.get(id_genero = genero)
		obj=Alumno.objects.create(rut=rut,
								nombre=nombre,
								apellido_paterno=aPaterno,
								apellido_materno=aMaterno,
								fecha_nacimiento=fechanac,
								id_genero=objGenero,
								telefono = telefono,
								email =email,)
		obj.save()
		context={'mensaje':"ok,datos grabados"}
		return render(request, 'home/alumnos_add.html')
	

