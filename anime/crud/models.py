#! coding: utf-8
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
