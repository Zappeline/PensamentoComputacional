
class ConversorMoeda:
    """Classe para converter preços entre moedas."""
    _COTACAO_USD_BRL = 5.05
    _COTACAO_EUR_BRL = 6.14
    _COTACAO_EUR_USD = 1.22
    

    def __init__(self, objeto_produto):
        """
        Inicializa o conversor de get_moeda() com o get_nome, preço, moeda e tipo do produto.
        """
        self.objeto_produto = objeto_produto


    def converte_preco_para_usd(self, Produtos) -> bool:
        """
        Converte o preço do produto para USD.
        Retorna True se a conversão foi feita, False se não foi necessária.
        Lança MoedaInvalidaError se a moeda não for reconhecida.
        """
        if Produtos.get_moeda() == "USD":
            print(f"O preço do produto '{Produtos.get_nome}' já está em USD. Nenhuma conversão necessária.")
            return False
        elif Produtos.get_moeda() == "BRL":
            Produtos.set_preco(Produtos.get_preco() / self._COTACAO_USD_BRL) 
            Produtos.set_moeda("USD")
            print(f"Preço de '{Produtos.get_nome()}' convertido de BRL para USD.")
            return True
        elif Produtos.get_moeda() == "EUR":
            Produtos.set_preco(Produtos.get_preco() / self._COTACAO_EUR_USD)
            Produtos.set_moeda("USD")
            print(f"Preço de '{Produtos.get_nome()}' convertido de EUR para USD.")
            return True
        else:
            print(f"Moeda inválida: {Produtos.get_moeda()}")

    def converte_preco_para_eur(self, Produtos) -> bool:
        """
        Converte o preço do Produtos para EUR.
        Retorna True se a conversão foi feita, False se não foi necessária.
        Lança get_moedaInvalidaError se a get_moeda() não for reconhecida.
        """
        if Produtos.get_moeda() == "EUR":
            print(f"O preço do Produtos '{Produtos.get_nome}' já está em EUR. Nenhuma conversão necessária.")
            return False
        elif Produtos.get_moeda() == "BRL":
            Produtos.set_preco(Produtos.get_preco / self._COTACAO_EUR_BRL)
            Produtos.set_moeda("EUR") 
            print(f"Preço de '{Produtos.get_nome()}' convertido de BRL para EUR.")
            return True
        elif Produtos.get_moeda() == "USD":
            Produtos.set_preco(Produtos.get_preco / self._COTACAO_EUR_USD)
            Produtos.set_moeda("EUR") 
            print(f"Preço de '{Produtos.get_nome()}' convertido de USD para EUR.")
            return True
        else:
            print(f"Moeda inválida: {Produtos.get_moeda()}")

    def converte_preco_para_brl(self, Produtos) -> bool:
        """
        Converte o preço do Produtos para BRL.
        Retorna True se a conversão foi feita, False se não foi necessária.
        Lança MoedaInvalidaError se a moeda não for reconhecida.
        """
        if Produtos.get_moeda() == "BRL":
            print(f"O preço do Produto '{Produtos.get_nome}' já está em BRL. Nenhuma conversão necessária.")
            return False
        elif Produtos.get_moeda() == "USD":
            Produtos.set_preco(Produtos.get_preco * self._COTACAO_USD_BRL)
            Produtos.set_moeda("BRL")
            print(f"Preço de '{Produtos.get_nome()}' convertido de USD para BRL.")
            return True
        elif Produtos.get_moeda() == "EUR":
            Produtos.set_preco(Produtos.get_preco * self._COTACAO_EUR_BRL )
            Produtos.set_moeda("BRL")
            print(f"Preço de '{Produtos.get_nome()}' convertido de EUR para BRL.")
            return True
        else:
            print(f"Moeda inválida: {Produtos.get_moeda()}")