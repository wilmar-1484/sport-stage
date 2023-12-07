from django.db import models
from django.db.models.base import Model

# Create your models here.
class LoginUsuarios(models.Model):
    nombre = models.CharField('Nombre', max_length=80, null="True")
    cedula = models.IntegerField('Cedula', null="True")
    direccion = models.CharField('Direccion', max_length=80, null="True")
    email = models.CharField('Email', max_length=80)
    clave = models.CharField('Clave', max_length=15)
    rol = models.CharField('Rol', max_length=50, null="True")

    
    class Meta:
        db_table = 'usuarios'

class escenariosReserva(models.Model):
    nombre=models.CharField('nombre',max_length=100)
    tipologia=models.CharField('tipologiaa',max_length=50)
    comuna=models.IntegerField('comuna')
    barrio=models.CharField('barrio',max_length=100)
    direccion=models.CharField('direccion',max_length=100)

    class Meta:
        db_table='escenarios'

class reservas(models.Model):
    id_usuario = models.ForeignKey(LoginUsuarios, on_delete=models.PROTECT )
    id_escenario = models.ForeignKey(escenariosReserva, on_delete=models.PROTECT)
    fecha = models.DateField ('Fecha',max_length=20)
    hora = models.CharField('Hora',max_length=20)
    
    class Meta:
        db_table = 'reservas'

  