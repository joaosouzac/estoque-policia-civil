from rest_framework import viewsets, mixins

from estoque.models import Objeto, Arma, Municao
from . import serializers


class ObjetoViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = serializers.ObjetoSerializer
    queryset = Objeto.objects.all()

class ArmaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArmaSerializer
    queryset = Arma.objects.all()

class MunicaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MunicaoSerializer
    queryset = Municao.objects.all()