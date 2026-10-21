from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
class Pista(models.Model):
    TIPO = [
        ("futbol", "Fútbol"),
        ("tenis", "Tenis"),
        ("baloncesto", "Baloncesto"),
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    pista = models.ForeignKey(Pista, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pista} - {self.usuario} - {self.fecha_inicio} - {self.fecha_fin}"

    def clean(self):
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_fin <= self.fecha_inicio:
                raise ValidationError("La hora de fin debe ser posterior a la de inicio.")
            choques = Reserva.objects.filter(pista=self.pista, fecha_inicio__lt=self.fecha_fin, fecha_fin__gt=self.fecha_inicio).exclude(pk=self.pk)
            if choques.exists():
                raise ValidationError("La pista no está disponible")