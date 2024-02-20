from rest_framework import serializers
from .models import Tarea

# Serialize: Crea un serializador llamado TareaSerializer que utilice el modelo Tarea y serialice todos los campos.


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class MinTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
