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
    
    def __str__(self):
        return str(self.nombreCompleto)
    
class portafolio(models.Model):
    nombrePortafolio = models.CharField(max_length=100)
    fechaIni = models.DateField(blank=False, null=False)
    infoPorta = models.CharField(max_length=700)
    
    def __str__(self):
        return str(self.nombrePortafolio)

class servicios(models.Model):
    nombreServicio = models.CharField(max_length=100)
    infoserv = models.CharField(max_length=700)
    
    def __str__(self):
        return str(self.nombreServicio)