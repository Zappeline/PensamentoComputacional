from .veiculo import Veiculo

class Frota:

    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo: Veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, veiculo: Veiculo):
        self.veiculos.remove(veiculo)

    def listar_veiculos_km(self, kilometros):
        consumo_total = 0
        for veiculo in self.veiculos:
            consumo_total += veiculo.get_consumo_by_km(kilometros)
        print(f"Consumo total da frota: {consumo_total} litros para {kilometros} km")
            #print(f"veiculo: ", {veiculo.nome}, "faz consumo de: ", veiculo.get_consumo_by_km(kilometros))

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(f"Veículo: {veiculo.nome}, Placa: {veiculo.get_placa()} Marca: {veiculo.marca}, Consumo: {veiculo.consumo} km/l")
