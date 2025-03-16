


from dominio.interfaces.ipedido import Pedido


class PedidoEnlatado(Pedido):
    def processar(self):
        print("Processando enlatado...")


class PedidoEnsacado(Pedido):
    def processar(self):
        print("Processando ensacado...")

    
class PedidoGranel(Pedido):
    def processar(self):
        print("Processando granel...")