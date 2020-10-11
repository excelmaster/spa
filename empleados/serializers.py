from rest_framework import serializers 
from empleados.models import Empleados

class EmpleadosSerializer(serializers.ModelSerializer):
    """
    docstring
    """
    class Meta:
        """
        docstring
        """
        model=Empleados
        fields=(
            'doc_emp',
            'nombres',
            'primerapellido',
            'segundoapellido',
            'email',
            'celu',
            'fechanacimiento','idservicio'
        )