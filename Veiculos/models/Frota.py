class Frota:
    Frota = []
    def __init__(self, Frota, distancia: int):
        self.Frota = Frota
        self.distancia = distancia
        
    def __str__(self):
        return f"Frota: {self.Frota} - Distância: {self.distancia}"