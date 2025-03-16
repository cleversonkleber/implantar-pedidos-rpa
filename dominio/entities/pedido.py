
from dataclasses import dataclass

@dataclass
class Item:
    item:int
    quantidade:int
    preco:float
    
@dataclass
class ProdutoEntity:
    codigo:int
    nome:str
    preco:float

@dataclass
class PedidoEntity:
    numero_pedido:int
    data_pedido:object
    items:[Type(Item)] # type: ignore

