from models.Veiculos import Veiculos
from models.Caminhoes import Caminhoes
from models.Motos import Motos
from models.Carros import Carros
from models.Frota import Frota

Focus = Carros("Focus", "Ford", "ABC1234", 2020, 50)
Xre = Motos("XRE", "Honda", "XYZ5678", 2021, "Preto", 100)
Caminhao = Caminhoes("Caminhao", "Mercedes", 2019, 10000, 60)

Frota = Frota()


Frota.adicionar_veiculo(Focus)
Frota.adicionar_veiculo(Xre)
Frota.adicionar_veiculo(Caminhao)


