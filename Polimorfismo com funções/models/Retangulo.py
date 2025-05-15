class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.__base = base
        self.__altura = altura

    def calcular_area(self) -> float:
        """
        Método que calcula a área do retângulo
        """
        return self.__base * self.__altura
        
    