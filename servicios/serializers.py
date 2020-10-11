from rest_framework import serializers 
from servicios.models import Servicios

class ServiciosSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model=Servicios
        fields=(
            'idservicio',
            'titulo',
            'descripcion',
            'image'
        )