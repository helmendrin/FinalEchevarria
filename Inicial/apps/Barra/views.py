from django.shortcuts import render
from .models import PedidosAbierto

def pedidos_abiertos_view(request):
    pedidos_abiertos = PedidosAbierto.objects.first()  # Assuming there's only one instance of PedidosAbierto, modify as per your requirement.
    return render(request, 'pedidos_abiertos.html', {'pedidos_abiertos': pedidos_abiertos})

