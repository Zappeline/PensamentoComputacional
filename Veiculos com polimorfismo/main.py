from models.carro import Carro
from models.moto import Moto
from models.frota import Frota
from models.caminhao import Caminhao
from models.carro_eletrico import Carro_eletrico

fox = Carro("Fox","HHH5555", "volkswagen")
xre = Moto("XRE", "AAA1111", "Honda")
truck = Caminhao("Truck", "", "Mercedes")
byd = Carro_eletrico("Seal", "", "BYD")

frota = Frota()

frota.adicionar_veiculo(fox)
frota.adicionar_veiculo(xre)
frota.adicionar_veiculo(truck)
frota.adicionar_veiculo(byd)

frota.listar_veiculos()

byd.recarrgar()

frota.listar_veiculos_km(100)

fox.set_placa("ABC1234")
byd.set_placa("AFH1534")
truck.set_placa("AAA1111")

frota.listar_veiculos()

xre.__eq__(truck)
xre.__eq__(fox)


