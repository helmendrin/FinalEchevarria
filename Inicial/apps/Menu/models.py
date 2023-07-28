from django.db import models


class Menu(models.Model):
    plato = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    platoPrecio = models.DictField()

    def __str__(self) -> str:
        return f"{self.plato} - ${self.precio}"
