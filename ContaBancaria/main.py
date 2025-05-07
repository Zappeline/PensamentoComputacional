from models.contas import Contas

Lucas = Contas("Lucas Zappeline", 1000, 500, [])

Ana = Contas("Ana Maria", 100, 50, [])

Lucas.depositar(150)
Lucas.exibir_historico()
Lucas.sacar(100)
Lucas.exibir_historico()
