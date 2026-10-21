from django.urls import path
from . import views

urlpatterns = [
    path("pistas/", views.lista_pistas, name="lista_pistas"),
]