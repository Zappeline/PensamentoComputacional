class Contas:
    def __init__(self, titular, saldo, limite, historico):
        self.limite = limite
        self.titular = titular
        self.saldo = saldo
        self.historico = historico

        

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print(f"O {valor} é inválido para depósito.")   

    def sacar(self, valor):
        if valor <= self.saldo: #Com saldo 
            self.saldo -= valor
            self.historico.append()
            print(f"Saque de {valor} realizado com sucesso.")
        else: #Sem saldo
            a = print(f"Deseja utilizar o limite de (R${self.limite}) [s para sim]?")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print(f"Saque de {valor} realizado com sucesso.")
                else:
                    print(f"Saldo insuficiente para o saque de {valor}.")
            else:
                print(f"Operação com limite cancelada.")


    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino += valor
            return True
        return False
    
    def exibir_historico(self):
    
    def exibir_saldo(self):