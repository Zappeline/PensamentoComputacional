class produtos:
    def __init__(self, nome: str, preco: float, moeda: str):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = moeda

    def __str__(self) -> str:
        '''Retorna uma string com as informações do veiculo'''
        infos = f"Nome: {self.__nome}\n"
        infos += f"Preço: {self.__preco}\n"
        infos += f"Moeda: {self.__moeda}\n"
        return infos
    
    
    