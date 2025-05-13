import time
from models.contas import Contas


# from datetime import datetime


banco = []

Lucas = Contas("Lucas", 1000, 100, [], ["044.171.580-02"])
banco.append(Lucas)
Leo = Contas("Leo", 100, 100, [], ["97768616"])
banco.append(Leo)

print("Bem-vindo!")

print("Sistema Bancário:")

while True:
    funcao = int(input("Menu bancario, digite a ação que deseja efetuar:\n" \
                "1- Criar conta\n2- Exibir saldo\n3- Sacar\n4- Depositar\n" \
                "5- Realizar transferencia\n6- Exibir historico\n7- Excluir conta\n8- Enviar via pix\n"
                "9- Sair\n"
                "Informe a opção:"))

    if funcao > 0 and funcao < 9:
        if funcao == 1:
            titular = input("Favor informar o nomê do titular:")
            chavepix_1= input("Favor informar a chave pix 1:")
            chavepix_2= input("Favor informar a chave pix 2:")
            chavepix_3= input("Favor informar a chave pix 3:")
            saldo = 0
            limite = 100
            historico = []
            conta = Contas(titular, saldo, limite, [], [chavepix_1, chavepix_2, chavepix_3])
            print(f"Conta criada com sucesso!, Você iniciou sua conta com um valor de: {limite} R$ de limite!")

            banco.append(conta)
            for conta in banco:
                if conta.getTitular() == titular:
                    print(f"O {titular} tem R$ {conta.saldo} em conta! e {limite} R$ de limite!")

        if funcao == 2:
            titular = input("Informe o nome do titular da conta que deseja ver o saldo:")
            encontrou = False
            for conta in banco:
                if conta.getTitular() == titular:
                    encontrou = True
                    print(conta)
            if not encontrou:
                resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                if resposta == "s":
                    break
                else:
                    print("Programa encerrado!")
                    break

        if funcao == 3:
            titular = input("Informe o nome do titular da conta que deseja sacar:")
            valor = float(input("Informe o valor que deseja sacar:"))
            for conta in banco:
                if conta.getTitular() == titular:
                    if valor > conta.saldo:
                        print("Valor maior que o saldo, saque não realizado!")
                    else:
                        conta.sacar(valor)
                        conta.saldo -= valor
                        print(f"Você sacou R$ {valor} da sua conta, seu saldo atual é de R$ {conta.saldo}")
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")
                        break
        
        if funcao == 4:
            titular = input("Informe o nome do titular da conta que deseja depositar:")
            valor = float(input("Informe o valor que deseja depositar:"))
            for conta in banco:
                if conta.getTitular() == titular:
                    conta.depositar(valor)
                    print(f"Você depositou R$ {valor} na sua conta, seu saldo atual é de R$ {conta.saldo}")
                    conta.saldo += valor
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")
           
        
        if funcao == 5:
            titular = input("Informe o nome do titular da conta que deseja transferir:")
            valor = float(input("Informe o valor que deseja transferir:"))
            destinatario = input("Informe o nome do destinatário:")
            encontrou = False
            for conta in banco:
                if conta.getTitular() == titular:
                    encontrou = True
                    if valor > conta.saldo:
                        print("Valor maior que o saldo, transferencia não realizada!")
                    else:
                        conta.transferir(valor, destinatario)
                        conta.saldo -= valor
                    for conta_destinatario in banco:
                        if conta_destinatario.titular == destinatario:
                            conta_destinatario.depositar(valor, titular)
                            conta_destinatario.saldo += valor
                            print(f"Você transferiu R$ {valor} para {destinatario}, seu saldo atual é de R$ {conta.saldo}")
                    else:
                        resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                        if resposta == "s":
                            break
                        else:
                            print("Programa encerrado!")
        if funcao == 6:
            titular = input("Informe o nome do titular da conta que deseja ver o histórico:")
            for conta in banco:
                if conta.getTitular() == titular:
                    print(f"Historico de {conta.getTitular()}:")
                    exibir_historico = conta.historico
                    for i in exibir_historico:
                        dt = time.localtime(i["data_e_tempo"])
                        print(f"Op:", i["operacao"],
                              "- Remetente:", i["remetente"],
                              "- Destinatario:", i["destinatario"],
                              "- Valor:", i["valor"],
                              "- Saldo:", i["saldo"],
                              "- Data e hora:", time.strftime("%d/%m/%Y %H:%M:%S", dt))
                else:   
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")

        if funcao == 7:
            titular = input("Informe o nome do titular da conta que deseja excluir:")
            for conta in banco:
                if conta.getTitular() == titular:
                    banco.remove(conta)
                    print(f"Conta de {titular} excluída com sucesso!")
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")

        if funcao == 8:
            titular = input("Informe o nome da sua conta titular:")
            for conta in banco:
                if conta.getTitular() == titular:
                    chavepix = input("Informe a chave pix do destinatário:")
                    valor = float(input("Informe o valor que deseja transferir:"))
                    if valor > conta.getSaldo():
                        print("Valor maior que o saldo, transferencia não realizada!")
                    else:
                        encontrou = False
                        for conta_destinatario in banco:
                            for chave in conta_destinatario.getChavePix():
                                if chave == chavepix:
                                    encontrou = True
                                    conta.sacar(valor,titular)
                                    conta_destinatario.depositar(valor, titular)
                                    print(f"Você enviou R$ {valor} via pix para {conta_destinatario.getTitular()}, seu saldo atual é de R$ {conta.getSaldo()}")
                        if not encontrou:
                            resposta = input("Conta não encontrada! Deseja consultar novamente? s/n:")
                            if resposta == "s":
                                break
                            else:
                                print("Programa encerrado!")
                                break

                    
    
        
        

    


