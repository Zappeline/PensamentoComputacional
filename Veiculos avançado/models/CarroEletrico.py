from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    ''' Classe que implementa métodos específicos de carros elétricos
    Argumento: Classe pai Veiculo
    '''

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,
                 nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int):
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia

    def __str__(self):
        infos = Veiculos.__str__(self)
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Nivel da bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}"
        return infos 
    
    def get_nivel_bateria(self):
        '''
        Objetivo: Método que retorna o nível da bateria do carro elétrico.
        return: nivel_bateria (int)
        '''
        return self.__nivel_bateria
    
    def get_tipo_bateria(self):
        '''
        Objetivo: Método que retorna o tipo da bateria do carro elétrico.
        return: tipo_bateria (str)
        '''
        return self.__tipo_bateria
    
    def get_autonomia(self):
        '''
        Objetivo: Método que retorna a autonomia do carro elétrico.
        return: autonomia (int)
        '''
        return self.__autonomia