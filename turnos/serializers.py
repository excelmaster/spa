from rest_framework import serializers 
from turno.models import Turnos

class TurnosSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model=Turnos
        fields=(
            'idturno',
            'dia',
            'hora',
            'docemp',
            'selecionado'
        )