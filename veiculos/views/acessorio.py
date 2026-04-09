from rest_framework.viewsets import ModelViewSet

from veiculos.models import Acessorio
from veiculos.serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
