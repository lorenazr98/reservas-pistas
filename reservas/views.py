from django.shortcuts import render, redirect
from .models import Pista
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required

def lista_pistas(request):
    pistas = Pista.objects.filter(activa=True)
    return render(request, "reservas/lista_pistas.html", {"pistas": pistas})

@login_required
def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect("lista_pistas")
    else:
        form = ReservaForm()
    return render(request, "reservas/crear_reserva.html", {"form": form})