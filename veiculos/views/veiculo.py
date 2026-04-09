from rest_framework.viewsets import ModelViewSet

from veiculos.models import Veiculo
from veiculos.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
