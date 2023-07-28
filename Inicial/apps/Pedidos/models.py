from django.db import models
from Menu import Menu
git 
# Create your models here.
class Pedido(models.Model):
    mesa = models.CharField(max_length=50)  # quisiera que quien toma el pedido pueda ingresar el nombre ( x ejemplo, maestra Cami 12hs, comisaria Raul 14 en punto)
    items = models.ManyToManyField(Menu, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Pedido {self.pk} - Mesa {self.mesa}"
    
    def add_pedido(self, mesa):
        pedido = Pedido.objects.create(mesa=mesa)
        self.pedidos.add(pedido)
        return pedido
