from django.db import models
from empleados.models import Empleados

# Create your models here.

class Turnos (models.Model):
    """
    docstring
    """


    idturno=models.AutoField(primary_key=True)
    dia=models.DateField( auto_now=True, auto_now_add=False)
    hora=models.TimeField( auto_now=True, auto_now_add=False)
    docemp=models.ForeignKey(Empleados, on_delete=models.CASCADE)
    seleccionado=models.IntegerField(0)