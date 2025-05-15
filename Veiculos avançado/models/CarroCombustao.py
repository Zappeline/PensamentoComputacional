from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    '''
    Classe que representa os veiculos do tipo combustao, que herda da classe Veiculos.
    '''
    
    def __init__(self, placa: str, modelo: str, marca: str, ano: int,
                 cor: str, valor_fipe: float, combustivel: str, nPortas: int,
                 nAssentos: int, nCilindradas: int, nCambio: str, nivel_combustivel: int) -> None:
        ''' Construtor da classe CarrosCombustao'''
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel

    def __str__(self) -> str:
        '''
        Retorna uma string com as informações do carro de combustão
        '''
        # Chama o método __str__ da classe pai (Veiculos)
        infos = Veiculos.__str__(self)
        # Adiciona as informações específicas do carro de combustão
        infos += f"combustivel: {self.__combustivel}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Cilindradas: {self.__nCilindradas}\n"
        infos += f"Cambio: {self.__nCambio}\n"
        infos += f"Nivel de combustivel: {self.__nivel_combustivel}\n"
        return infos

    def abastecer(self, percentual_adicionado: int) -> bool:
        '''
        Metodo para abastecer um carro a combustão

        Argumentos: Percentual (int) percentual adicionado

        Retorno: 
            bool: True se foi possivel abastecer, e false caso contrario

        '''
        novo_percentual = self.__nivel_combustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False
    
    