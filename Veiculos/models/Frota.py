class Frota:
    
    def __init__(self):
        self.__Frota = []
        

    def adicionar_veiculo(self, veiculo):
        self.__Frota.append(veiculo)
    
    def remover_veiculo(self, veiculo):
        self.__Frota.remove(veiculo)
    
    def consumoTotal(self, distancia):
        consumo_total = 0
        for veiculo in self.__Frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total
    
    def listar_veiculos(self):
        for veiculo in self.__Frota:
            print(veiculo)