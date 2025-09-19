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


cliente = Cliente("kleber", "SP")
item_um = Item("Pizza", 30.0)
item_dois = Item("Regrigerante", 5.0)
itens = [item_um, item_dois]

pedido_retirada = PedidoRetirada(cliente, itens)

taxa_entrega = 10.0
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido_delivery.calcular_total()
# pagamento_cartao = PagamentoCartao().processar(valor_pedido)
# pagamento_pix = PagamentoPIX()
# pagamento_pix.processar(valor_pedido)

tipo_pagamento = "pix"
pagamento = PagamentoFactory

MENSAGEM = "Seu pedido saiu para entrega!"
# notificacao_email = NotificacaoEmail().enviar_notificacao(cliente, MENSAGEM)
# notificacao_sms = NotificacaoSMS().enviar_notificacao(cliente, MENSAGEM)

notificacoes = NotificacaoFacade().enviar_notificacoes(cliente, MENSAGEM)
