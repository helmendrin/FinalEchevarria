from django.db import models
from Menu import Menu
from Pedidos import Pedido


class PedidosAbierto(models.Model):
    pedidos = models.ManyToManyField(Pedido, related_name='pedidos_abiertos')

    def __str__(self) -> str:
        return f"Pedidos Abiertos: {self.pedidos.count()}"

    


