from .veiculo import Veiculo

class Carro_eletrico(Veiculo):

    def __init__(self, nome, placa, marca): 
        super().__init__(nome, placa, marca, 0.15)

    def get_consumo_by_km(self, kilometros):
        consumo = kilometros / self.consumo
        print(f"Em {kilometros}Km, O consumo do veiculo {self.nome} da marca: {self.marca} é de {consumo} kWh/km")
        return consumo
    
    def recarrgar (self):
        print("A bateria foi regarregada")