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
    
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> str:
        self.__nome = nome
        print(f"O produto alterou o nome para {self.__nome}")

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco) -> float:
        self.__preco = preco
        print(f"O produto alterou o preco para {self.__preco}")

    def get_moeda(self) -> str:
        return self.__moeda

    def set_moeda(self, moeda) -> str:
        self.__moeda = moeda
        print(f"O produto alterou o moeda para {self.__moeda}")

####################################################################################

class ProdutoEletronico:
    def __init__(self, nome: str, preco: float, moeda: str):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = moeda

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
    
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> str:
        self.__nome = nome
        print(f"O produto alterou o nome para {self.__nome}")

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco) -> float:
        self.__preco = preco
        print(f"O produto alterou o preco para {self.__preco}")

    def get_moeda(self) -> str:
        return self.__moeda

    def set_moeda(self, moeda) -> str:
        self.__moeda = moeda
        print(f"O produto alterou o moeda para {self.__moeda}")

#################################################################################

class ProdutoAlimnticio:
    def __init__(self, nome: str, preco: float, moeda: str):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = moeda

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
    
    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> str:
        self.__nome = nome
        print(f"O produto alterou o nome para {self.__nome}")

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco) -> float:
        self.__preco = preco
        print(f"O produto alterou o preco para {self.__preco}")

    def get_moeda(self) -> str:
        return self.__moeda

    def set_moeda(self, moeda) -> str:
        self.__moeda = moeda
        print(f"O produto alterou o moeda para {self.__moeda}")

    