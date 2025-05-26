from models.Produtos import Produtos
from models.ProdutoAlimenticio import ProdutoAlimnticio 
from models.ProdutoEletronico import ProdutoEletronico
from models.ConversorMoeda import ConversorMoeda

conversor = ConversorMoeda(Produtos)

refrigerante = Produtos("", 9.80, "BRL", "Alimenticio")

pao = ProdutoAlimnticio ("Pão", 5.70, "BRL", "Alimenticio")

radio = ProdutoEletronico("JBL", 59.60, "BRL", "Eletronico")

print(refrigerante)
refrigerante.set_nome("guarana")
print(pao)
refrigerante.set_preco(9.99)
print(refrigerante)
pao.set_preco(9.99)
print(pao)
print(radio)

conversor.converte_preco_para_usd(refrigerante)

print(refrigerante)