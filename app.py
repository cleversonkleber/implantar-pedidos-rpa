from dominio.services.factory_pedido import PedidoEnlatadoFactory,PedidoGranelFactory, PedidoEnsacadoFactory


def processar_pedidos(factory):
    pedido = factory.criar_pedido()
    pedido.processar()


if __name__=="__main__":
    processar_pedidos(PedidoEnlatadoFactory())
    processar_pedidos(PedidoEnsacadoFactory())
    processar_pedidos(PedidoGranelFactory())