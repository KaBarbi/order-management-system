from abc import ABC, abstractmethod


class Notificacao(ABC):
    @abstractmethod
    def enviar_notificacao(self, cliente, mensagem):
        pass

    @abstractmethod
    def enviar_email(self, cliente, mensagem):
        print("Enviar email")

    @abstractmethod
    def enviar_sms(self, cliente, mensagem):
        print("Enviar sms")
