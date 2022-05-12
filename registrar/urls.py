from django.urls import path

from . import views


app_name = "registrar"

urlpatterns = [
    path("armas/", views.ArmaCreate.as_view(), name="arma_create"),

]