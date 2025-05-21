class Carros:
    def __init__(self, modelo, marca, placa, ano, distancia):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.distancia = distancia

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Placa: {self.placa}"
    
    def calcular_consumo(self, distancia):
        self.distancia = distancia
        calcular_consumo = distancia / 12
        return print(f"Litros de combustível para {distancia} km: {calcular_consumo} L")
    
    