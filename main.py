from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSms
from notificacao.notificacao_facade import NotificacaoFacade

# Criando cliente e itens
cliente = Cliente("Kleber", "SP")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
itens = [item_um, item_dois]

# Criando pedidos
pedido_retirada = PedidoRetirada(cliente, itens)
taxa_entrega = 10.0
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

# Calculando valor total do pedido
valor_pedido = pedido_delivery.calcular_total()

# Processando pagamento usando Factory
tipo_pagamento = "pix"
pagamento = PagamentoFactory().criar_pagamento(tipo_pagamento)
pagamento.processar(valor_pedido)

# Enviando notificações usando Facade
MENSAGEM = "Seu pedido saiu para entrega!"
notificacao_facade = NotificacaoFacade()
notificacao_facade.enviar_notificacoes(cliente, MENSAGEM)

# Atualizando status do pedido e notificando novamente
pedido_delivery.status = "Pedido confirmado!"
notificacao_facade.enviar_notificacoes(cliente, pedido_delivery.status)
