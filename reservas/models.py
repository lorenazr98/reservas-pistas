from django.db import models

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