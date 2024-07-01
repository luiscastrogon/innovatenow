from django.db import models

# Create your models here.


class navbarmenu(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.nombre)
    
    
class staff(models.Model):
    nombreCompleto = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    soy = models.CharField(max_length=700)
    foto = models.ImageField(upload_to='static/images/', default='default.png')
    
    def __str__(self):
        return str(self.nombreCompleto)
    
class portafolio(models.Model):
    nombrePortafolio = models.CharField(max_length=100)
    fechaIni = models.DateField(blank=False, null=False)
    infoPorta = models.CharField(max_length=700)
    
    def __str__(self):
        return str(self.nombrePortafolio)

class servicio(models.Model):
    nombreServicio = models.CharField(max_length=100)
    infoserv = models.CharField(max_length=700)
    
    def __str__(self):
        return str(self.nombreServicio)    
       
class Genero(models.Model):
    id_genero = models.AutoField(db_column="idGenero", primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)