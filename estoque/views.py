from django.views.generic import DetailView, ListView

from .models import Arma, Municao


class ArmaListView(ListView):
    model = Arma

class ArmaDetailView(DetailView):
    model = Arma

class MunicaoListView(ListView):
    model = Municao

class MunicaoDetailView(DetailView):
    model = Municao