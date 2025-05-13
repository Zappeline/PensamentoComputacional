import time

class Contas:
    '''
    Classe que implementa métodos para manipular uma conta bancaria.add()
    Atributos: titular (str), saldo (float), limite (float), historico (lista de dicionários)

    Obs: Operações no historico: 0 - sacar, 1 - depositar, 2 - transferir

    '''

    def __init__(self, titular:str, saldo: float, limite: float, historico: list) -> None:  
        ''' 
        Construtor da classe ContaBancaria
        ''' 
        self.__limite = limite
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = historico
        

    def __str__(self):
        return f"Titular: {self.__titular}, Saldo: {self.__saldo}, Limite: {self.__limite}"

    def getTitular(self):
        '''
        Objetivo: Método que retorna o titular da conta bancaria.
        return: titular (str)
        '''
        return self.__titular

    def depositar(self, valor, remetente = None):
        '''
        Objetivo: Método que implementar o depósito na conta bancaria.
        Entradas: valor (float) e remetente (str).
        return: True, se o depósito for realizado com sucesso. False, caso contrário.
        '''
        op = 1 #Detecta que é uma transferencia
        if remetente != None:
            op = 2
        if valor > 0:
            self.__saldo += valor
            self.__historico.append({"operacao": op,
                                   "remetente": remetente,
                                   "destinatario": self.__titular,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "data_e_tempo": int(time.time())})
            return True
        else:
            print(f"O {valor} é inválido para depósito.")   
            return False

    def sacar(self, valor, destinatario = None):
        '''
        Objetivo: Método que implementar o saque na conta bancaria.
        Entradas: valor (float) e destinatario (str)
        return: True, se o saque for realizado com sucesso. False, caso contrário.
        '''
        op = 0 #Detecta que é uma transferencia e muda a operação para 2
        if destinatario != None:
            op = 2
        if valor <= self.__saldo: #Com saldo 
            self.__saldo -= valor
            self.__historico.append({"operacao": op,
                                   "remetente": self.__titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "data_e_tempo": int(time.time())})
            print(f"Saque de {valor} realizado com sucesso.")
            return True
        
        else: #Sem saldo
            a = print(f"Deseja utilizar o limite de (R${self.__limite}) [s para sim]?")
            if a == 's':
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    print(f"Saque de {valor} realizado com sucesso.")
                else:
                    print(f"Saldo insuficiente para o saque de {valor}.")
            else:
                print(f"Operação com limite cancelada.")
                return False
            
    def transferir(self, destinatario, valor):
        '''
        Objetivo: Método que implementar a transferência entre contas bancarias.
        Entradas: valor (float) e obj conta do destinatario
        saida: True, se a transferência for realizada com sucesso. False, caso contrário.
        '''

        # Se o saque ocorrer com sucesso.
        if self.sacar(valor, destinatario.titular): #Saca o valor da conta do remetente
            # Deposita o valor na conta do destinatario
            destinatario.depositar(valor, self.__titular) #Deposita o valor na conta do destinatario

        
             
    def exibir_historico(self):
        print(f"Historico de transações da conta {self.__titular}:")
        for transacao in self.__historico:
            dt = time.localtime(transacao["data_e_tempo"])
            print(f"Op:", transacao["operacao"],
                   "- Remetente:", transacao["remetente"],
                   "- Destinatario:", transacao["destinatario"],
                   "- Valor:", transacao["valor"],
                   "- Saldo:", transacao["saldo"], 
                   "- Data e Hora:", (f"{dt.tm_mday}/{dt.tm_mon}/{dt.tm_year}"), "-", #1° Maneira de formatar
                   str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec))     #2° Maneira de formatar
    
        


     