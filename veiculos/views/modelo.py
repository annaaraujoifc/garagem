from rest_framework.viewsets import ModelViewSet

from veiculos.models import Modelo
from veiculos.serializers import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
