from abc import ABC, abstractmethod


class PedidoFactory(ABC):
    @abstractmethod
    def criar_pedido(self):
        pass