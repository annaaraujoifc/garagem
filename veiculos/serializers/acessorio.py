from rest_framework import serializers

from veiculos.models import Acessorio


class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'
