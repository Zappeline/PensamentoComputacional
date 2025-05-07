import time

class Contas:
    '''
    Classe que implementa métodos para manipular uma conta bancaria.add()
    Atributos: titular (str), saldo (float), limite (float), historico (lista de dicionários)

    Obs: Operações no historico: 0 - sacar, 1 - depositar, 2 - transferir

    '''

    def __init__(self, titular, saldo, limite, historico):
        ''' 
        Construtor da classe ContaBancaria
        ''' 
        self.limite = limite
        self.titular = titular
        self.saldo = saldo
        self.historico = historico

        

    def depositar(self, valor):
        '''
        Objetivo: Método que implementar o depósito na conta bancaria.
        Entrada: valor (float)
        return: True, se o depósito for realizado com sucesso. False, caso contrário.
        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": 1,
                                   "remetente": self.titular,
                                   "destinatario": None,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data_e_tempo": int(time.time())})
            return True
        else:
            print(f"O {valor} é inválido para depósito.")   
            return False

    def sacar(self, valor):
        '''
        Objetivo: Método que implementar o saque na conta bancaria.
        Entrada: valor (float)
        return: True, se o saque for realizado com sucesso. False, caso contrário.
        '''
        if valor <= self.saldo: #Com saldo 
            self.saldo -= valor
            self.historico.append({"operacao": 0,
                                   "remetente": self.titular,
                                   "destinatario": None,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data_e_tempo": int(time.time())})
            print(f"Saque de {valor} realizado com sucesso.")
            return True
        
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
                return False
             
    def exibir_historico(self):
        print(f"Historico de transações da conta {self.titular}:")
        for transacao in self.historico:
            dt = time.localtime(transacao["data_e_tempo"])
            print(f"Op:", transacao["operacao"],
                   "- Remetente:", transacao["remetente"],
                   "- Destinatario:", transacao["destinatario"],
                   "- Valor:", transacao["valor"],
                   "- Saldo:", transacao["saldo"], 
                   "- Data e Hora:", (f"{dt.tm_mday}/{dt.tm_mon}/{dt.tm_year}"), "-", #1° Maneira de formatar
                   str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec))     #2° Maneira de formatar

    def transferir(self, valor, destinatario):
        '''
        Objetivo: Método que implementar a transferência entre contas bancarias.
        Entrada: valor (float), destinatario (str)
        return: True, se a transferência for realizada com sucesso. False, caso contrário.
        '''
        if valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor
            self.historico.append({"operacao": 2,
                                   "remetente": self.titular,
                                   "destinatario": destinatario.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data_e_tempo": int(time.time())})
            print(f"Transferência de {valor} para {destinatario.titular} realizada com sucesso.")
            return True
        else:
            print(f"Saldo insuficiente para a transferência de {valor}.")
            return False       

     