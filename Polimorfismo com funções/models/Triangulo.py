class Triangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Método que calcula a área do triângulo
        """
        return (self.base * self.altura) / 2
    