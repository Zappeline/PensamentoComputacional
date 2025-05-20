from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao  
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico


voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)

jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen", 2025, "Vermelho",
                            250000, "Gasolina", 4, 5, 2000, "AT 7", 24)

tesla_model_s = CarroEletrico("JDNA00", "Tesla Model S", "Tesla", 2021, "Branco", 950000,
                               5, 4, 65, "Lítio", 491)

fusca_eletrico = CarroConvEletrico(placa="IAA0D36",           modelo="Fusca 1600 Eletrico", 
                                   marca="Volkswagen",        ano=1975, 
                                   cor="Azul",                valor_fipe=70000, 
                                   combustivel="Gasolina",    nPortas=4, 
                                   nAssentos=5,               nCilindradas=1600, 
                                   nCambio="MT 4",            nivel_combustivel=None, 
                                   nivel_bateria=65,          tipo_bateria="Lítio", 
                                   autonomia=150)

''' informação (laranja), caso preferir para não se perder'''


print(fusca_eletrico)

fusca_eletrico.abastecer(20)