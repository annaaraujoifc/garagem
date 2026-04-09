from rest_framework.viewsets import ModelViewSet

from veiculos.models import Cor
from veiculos.serializers import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
