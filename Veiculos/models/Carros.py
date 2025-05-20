class Carros:
    def __init__(self, modelo, marca, placa, ano):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"
    
    def litros_distancia(self, distancia):
        self.distancia = distancia
        litros_distancia = distancia / 12
        return print(f"Litros de combustível para {distancia} km: {litros_distancia} L")
    
    