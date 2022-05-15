from django.db import models
from django.contrib.auth.models import User

class Instrumento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    tipoInstrumento = models.CharField(max_length=40, null=True, blank=True)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    esFavorito = models.BooleanField(default=False)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()

    def __str__(self):
        return self.titulo

