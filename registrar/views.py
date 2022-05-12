from django.views.generic import CreateView
from django.urls import reverse_lazy

from estoque.models import Arma


class ArmaCreate(CreateView):
    model = Arma
    fields = ["calibre_id", "marca", "modelo", "quantidade_de_tiros", "valor_estimado"]
    template_name = "registrar/form.html"
    success_url = reverse_lazy("arma_list")
