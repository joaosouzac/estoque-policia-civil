from django.urls import path

from . import views


app_name = "estoque"

urlpatterns = [
    path("armas/", views.ArmaListView.as_view(), name="arma_list"),
    path("armas/<int:pk>", views.ArmaDetailView.as_view(), name="arma_detail"),
    path("municoes/", views.MunicaoListView.as_view(), name="municao_list"),
    path("municoes/<int:pk>", views.MunicaoDetailView.as_view(), name="municao_detail"),
]