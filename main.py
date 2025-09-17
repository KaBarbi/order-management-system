from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada


cliente = Cliente("kleber", "SP")
item_um = Item("Pizza", 30.0)
item_dois = Item("Regrigerante", 5.0)
itens = [item_um, item_dois]

pedido_retirada = PedidoRetirada(cliente, itens)
print(f"Preco do pedido retirada: {pedido_retirada.calcular_total():.2f}")
