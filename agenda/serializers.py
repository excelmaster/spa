from rest_framework import serializers 
from agenda.models import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model=Agenda
        fields=(
            'idagenda',
            'idturno',
            'doccliente',
            'descricion'
        )