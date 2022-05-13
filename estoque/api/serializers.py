from rest_framework import serializers

from estoque.models import Objeto, Arma, Municao


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = "__all__"

class ArmaSerializer(serializers.ModelSerializer):
    imagem = serializers.ImageField(max_length=None, allow_empty_file=True, 
                                    allow_null=False, use_url=True, required=False)

    class Meta:
        model = Arma
        fields = ("id", "calibre_id", "marca", "modelo", "quantidade_de_tiros", 
                    "valor_estimado", "imagem")
        extra_kwargs = {"id": {"read_only": True},}

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municao
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True},}