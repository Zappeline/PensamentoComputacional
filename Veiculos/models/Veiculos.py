from .Caminhoes import Caminhoes
from .Carros import Carros
from .Motos import Motos
from .Frota import Frota


class Veiculos(Caminhoes, Motos, Carros, Frota):

    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longetude): 
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
        Caminhoes.__init__(self, modelo, marca, ano, 0, 0, 0)
        self.capacidade_carga = 0
        self.distancia = 0
        Carros.__init__(self, modelo, marca, placa, ano, 0, 0)
        self.distancia = 0
        Motos.__init__(self, modelo, marca, placa, ano, cor, 0, 0)
        self.distancia = 0
        Frota.__init__(self,)
        self.__veiculos = []

       
        
        


    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa} - Cor: {self.cor} - Velocidade: {self.velocidade} km/h - Latitude: {self.latitude} - Longitude: {self.longetude}"



        
    
    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterar_latitude(nova_latitude)
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O veiculo de placa {self.placa} freiou até {self.velocidade} km/h")

    def mostrar_infos(self):
        print(f"O veiculo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h")
        print(f"Lat: {self.latitude}, Long: {self.longetude}")

    def alterar_placa(self, placa):
        self.placa = placa

    def alterar_ano(self, ano):
        self.ano = ano

    def alterar_cor(self, cor):
        self.cor = cor
    
    def alterar_latitude(self, latitude):
        self.latitude = latitude

    def alterar_longetude(self, longetude):
        self.longetude = longetude

    def litros_distancia(self, distancia, consumo):
        litros_distancia = distancia / consumo
        return litros_distancia
    