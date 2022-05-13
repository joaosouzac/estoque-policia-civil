from rest_framework import viewsets

from estoque.models import Objeto, Arma, Municao
from . import serializers


class ObjetoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObjetoSerializer
    queryset = Objeto.objects.all()

class ArmaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArmaSerializer
    queryset = Arma.objects.all()

class MunicaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MunicaoSerializer
    queryset = Municao.objects.all()