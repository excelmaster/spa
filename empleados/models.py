from django.db import models
from servicios.models import Servicios

# Create your models here.

class Empleados(models.Model):
    """
    docstring
    """
    docemp=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=70,blank=False, null=False)
    primerapellido=models.CharField(max_length=70,blank=False, null=False)
    segundoapellido=models.CharField(max_length=70,blank=False, null=False)
    email=models.CharField(max_length=70,blank=False, null=False)
    celu=models.CharField(max_length=70,blank=False, null=False)
    fechanacimiento=models.DateField(auto_now=True, auto_now_add=False)
    # TODO: ENPLEADOS
    idservicio=models.ForeignKey(Servicios,  on_delete=models.CASCADE)


