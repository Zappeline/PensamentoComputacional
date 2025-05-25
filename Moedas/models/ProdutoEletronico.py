from .Produtos import Produtos

class ProdutoEletronico(Produtos):
    def __init__(self, nome: str, preco: float, moeda: str, tipo: str):
        super().__init__(nome, preco, moeda, tipo) 

    def __str__(self):
        infos = super().__str__()
        return infos

    