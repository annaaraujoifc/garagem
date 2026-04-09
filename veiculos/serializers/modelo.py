from rest_framework import serializers

from veiculos.models import Modelo


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'
