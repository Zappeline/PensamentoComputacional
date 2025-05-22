from .veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, nome, placa, marca): 
        super().__init__(nome, placa, marca, 20)