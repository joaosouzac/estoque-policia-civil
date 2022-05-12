from django.db import models
from django.urls import reverse


class ObjetoTipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_de_objeto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        if self.tipo_de_objeto == None:
            return "Sem Tipo"
        else:
            return self.tipo_de_objeto

class Objeto(models.Model):
    id = models.BigAutoField(primary_key=True)
    objeto_tipo_id = models.ForeignKey(ObjetoTipo, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.id)

class Calibre(models.Model):
    id = models.AutoField(primary_key=True)
    desc_calibre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        if self.desc_calibre == None:
            return "Sem Calibre"
        else:
            return self.desc_calibre

class Arma(models.Model):
    id = models.OneToOneField(Objeto, on_delete=models.CASCADE, primary_key=True)
    calibre_id = models.ForeignKey(Calibre, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    quantidade_de_tiros = models.IntegerField(blank=True, null=True)
    valor_estimado = models.FloatField(blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("estoque:arma_detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        if self.modelo == None:
            return "Arma Genérica (Sem Modelo)"
        else:
            return self.modelo


class Municao(models.Model):
    id = models.OneToOneField(Objeto, on_delete=models.CASCADE, primary_key=True)
    calibre_id = models.ForeignKey(Calibre, on_delete=models.CASCADE)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    valor_estimado = models.FloatField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("estoque:municao_detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        if self.modelo == None:
            return "Munição Genérica (Sem Modelo)"
        else:
            return self.modelo
