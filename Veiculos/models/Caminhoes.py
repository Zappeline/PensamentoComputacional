class Caminhoes:
    def __init__(self, marca:str, modelo:str, ano:int, capacidade_carga:float, distancia: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidade_carga = capacidade_carga
        self.distancia = distancia


    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Capacidade de Carga: {self.capacidade_carga} kg {self.consumo} km/l {self.distancia} km"
    
    def litros_distancia(self, distancia):
        litros_distancia = distancia / 5
        return print(f"Litros de combustível para {distancia} km: {litros_distancia} L")