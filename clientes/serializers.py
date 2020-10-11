from rest_framework import serializers 
from clientes.models import Clientes

class ClienteSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model=Clientes
        fields=(
            'doc_cliente',
            'nombre',
            'primerapellido',
            'segundoapellido',
            'email',
            'celu',
            'fechanacimiento'
        )