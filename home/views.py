from django.shortcuts import render
from .models import navbarmenu
from .models import staff

# Create your views here.

def index(request):
	navbarmenus = navbarmenu.objects.all()
	context = { "navbarmenus": navbarmenus }	
	return render (request, 'home/index.html', context)

def index2(request):
	navbarmenus = navbarmenu.objects.all()
	context = { "navbarmenus": navbarmenus }	
	return render (request, 'quien/index2.html', context)

def index3(request):
	navbarmenus = navbarmenu.objects.all()
	context = { "navbarmenus": navbarmenus }	
	return render (request, 'servicios/index3.html', context)
	
def staff1(request):
    staffs = staff.objects.all()
    context = { "staffs": staffs }
    return render (request, 'quien/index2.html', context)

def servicios(request):
    servicio = servicios.objects.all()
    context = { "servicio": servicio }
    return render (request, 'servicios/index3.html', context)