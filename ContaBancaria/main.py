from models.contas import Contas

Lucas = Contas(nome_conta="Lucas Zappeline", saldo=1000, limite=500, historico=[])

Lucas.depositar(500)
Lucas.depositar(500)
Lucas.depositar(500)
Lucas.sacar(200)
Lucas.historico
Lucas.transferir(200, "Conta do João")

Lucas.historico
Lucas.saldo()
