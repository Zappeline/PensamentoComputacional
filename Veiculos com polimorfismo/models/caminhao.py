from .veiculo import Veiculo

class Caminhao(Veiculo):

    def __init__(self, nome, placa, marca): 
        super().__init__(nome, placa, marca, 5)