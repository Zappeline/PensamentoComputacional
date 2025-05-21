class Motos:
    def __init__(self, modelo, marca, placa, ano, cor, distancia): 
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor 
        self.distancia = distancia
        
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}): Placa: {self.placa}"
    
    def calcular_consumo(self, distancia):
        calcular_consumo = distancia / 20
        return print(f"Litros de combustível para {distancia} km: {calcular_consumo} L")