from django.db import models
from turnos.models import Turnos
from clientes.models import Clientes


# Create your models here.

class Agenda(models.Model):
    """
    docstring
    """
    idagenda=models.AutoField(primary_key=True)
    idturno=models.ForeignKey(Turnos,  on_delete=models.CASCADE)
    doccliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    descricion=models.CharField(max_length=150,blank=False,null=False)