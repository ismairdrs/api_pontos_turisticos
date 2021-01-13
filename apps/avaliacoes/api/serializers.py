from rest_framework import serializers
from apps.avaliacoes.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'comentario', 'nota', 'data')
