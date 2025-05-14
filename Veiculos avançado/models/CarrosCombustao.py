from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    '''
    Classe que representa os veiculos do tipo combustao, que herda da classe Veiculos.
    '''
    
    def __init__(self, placa: str, modelo: str, marca: str, ano: int,
                 cor: str, valor_fipe: float, combustivel: str, nPortas: int,
                 nAssentos: int, nCilindradas: int, nCambio: str) -> None:
        ''' Construtor da classe CarrosCombustao'''
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio

    def __str__(self) -> str:
        '''
        Retorna uma string com as informações do carro de combustão
        '''
        # Chama o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações específicas do carro de combustão
        infos += f"combustivel: {self.__combustivel}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Cilindradas: {self.__nCilindradas}\n"
        infos += f"Cambio: {self.__nCambio}\n"
        return infos
