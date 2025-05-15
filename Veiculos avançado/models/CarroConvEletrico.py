from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarroCombustao, CarroEletrico):
    '''
    Classe que implementa métodos especificos de um carro convertido
    em Elétrico
    '''
    def __init__(self, placa: str, modelo: str, marca: str, ano: int,
                 cor: str, valor_fipe: float, combustivel: str, nPortas: int,
                 nAssentos: int, nCilindradas: int, nCambio: str, nivel_combustivel: int,
                 nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        
        # No lugar do SUPER poderia ser CarroCombustão, SUPER é sempre o primeiro import
        CarroCombustao.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, combustivel,
                         nPortas, nAssentos, nCilindradas, nCambio, nivel_combustivel)
        CarroEletrico.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, nAssentos, nPortas,
                               nivel_bateria, tipo_bateria, autonomia)
        
    def __str__(self) -> str:
        infos = CarroCombustao.__str__(self)
        infos += f"Nivel de bateria: {CarroEletrico.get_nivel_bateria(self)}\n"
        infos += f"Tipo de bateria: {CarroEletrico.get_tipo_bateria(self)}\n"
        infos += f"Autonomia: {CarroEletrico.get_autonomia(self)}\n"
        return infos
    
    def abastecer(self, percentual_adicionado):
        """
        Metodo abastecer desativado
        argumento: percentual_adicionado

        Retorno:
            False, pois carro não pode abastecer
        """
        print("Carro convertido para Elétrico! Não é possivel mais abastece-lo!")
        return False
