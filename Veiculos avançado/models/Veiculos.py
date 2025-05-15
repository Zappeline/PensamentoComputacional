class Veiculos:
    '''
    Classe com os principais funcionalidades do sistema de veiculos,
    como placas, marca, modelo, ano, etc.'''

    def __init__(self, placa: str, modelo: str, marca: str, ano: int,
                  cor: str, valor_fipe: float) -> None:
        ''' Construtor da classe Veiculos'''
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe


    def __str__(self) -> str:
        '''Retorna uma string com as informações do veiculo'''
        infos = f"placa: {self.__placa}\n"
        infos += f"modelo: {self.__modelo}\n"
        infos += f"marca: {self.__marca}\n"
        infos += f"ano: {self.__ano}\n"
        infos += f"cor: {self.__cor}\n"
        infos += f"valor fipe: {self.__valor_fipe}\n"
        return infos
    

    def getPlaca(self) -> str:
        '''
        Objetivo: Método que retorna a placa do veiculo.
        return: placa (float)
        '''
        return self.__placa
    
    def setValorFipe(self, valor: float) -> None:
        '''
        Objetivo: Método que altera o valor da fipe do veiculo.
        valor: valor (float) : novo valor da fipe
        Saída: True se ok
        '''
        self.__valor_fipe = valor
        return True
    

