
from dominio.interfaces.ifactory_pedido import PedidoFactory
from dominio.services.pedido_empl import PedidoEnlatado, PedidoEnsacado, PedidoGranel


class PedidoEnlatadoFactory(PedidoFactory):
    def criar_pedido(self):
        return PedidoEnlatado()


class PedidoEnsacadoFactory(PedidoFactory):
    def criar_pedido(self):
        return PedidoEnsacado()
    
class PedidoGranelFactory(PedidoFactory):
    def criar_pedido(self):
        return PedidoGranel()