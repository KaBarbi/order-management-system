from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery


cliente = Cliente("kleber", "SP")
item_um = Item("Pizza", 30.0)
item_dois = Item("Regrigerante", 5.0)
itens = [item_um, item_dois]

pedido_retirada = PedidoRetirada(cliente, itens)

taxa_entrega = 10.0
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)
print(f"Preco do pedido delivery: {pedido_delivery.calcular_total():.2f}")
