from rest_framework import viewsets
from apps.atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
