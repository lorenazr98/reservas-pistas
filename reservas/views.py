from django.shortcuts import render
from .models import Pista

def lista_pistas(request):
    pistas = Pista.objects.filter(activa=True)
    return render(request, "reservas/lista_pistas.html", {"pistas": pistas})