from rest_framework import serializers

from estoque.models import Objeto, Arma, Municao


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = "__all__"

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True},}

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True},}