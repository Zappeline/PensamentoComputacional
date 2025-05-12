import time
from models.contas import Contas


# from datetime import datetime


banco = []

print("Sistema Bancário")

while True:
    funcao = int(input("Menu bancario, digite a ação que deseja efetuar:\n" \
                "1- Criar conta\n2- Exibir saldo\n3- Sacar\n4- Depositar\n" \
                "5- Realizar transferencia\n6- Exibir historico\n7- Excluir conta\n"
                "8- Sair\n"
                "Informe a opção:"))

    if funcao > 0 and funcao < 7:
        if funcao == 1:
            titular = input("Favor informar o nomê do titular:")
            saldo = 0
            limite = 100
            print(f"Conta criada com sucesso!, Você iniciou sua conta com um valor de: {limite} R$ de limite!")
            banco.append(Contas(titular, saldo, limite, []))

            for conta in banco:
                if conta.titular == titular:
                    print(f"O {titular} tem R$ {conta.saldo} em conta! e {limite} R$ de limite!")

        if funcao == 2:
            titular = input("Informe o nome do titular da conta que deseja ver o saldo:")
            for conta in banco:
                if conta.titular == titular:
                    print(f"O {titular} tem R$ {conta.saldo} em conta! e {limite} R$ de limite!")
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")

        if funcao == 3:
            titular = input("Informe o nome do titular da conta que deseja sacar:")
            valor = float(input("Informe o valor que deseja sacar:"))
            for conta in banco:
                if conta.titular == titular:
                    if valor > conta.saldo:
                        print("Valor maior que o saldo, saque não realizado!")
                        conta.valor -= conta.saldo
                    else:
                        conta.sacar(valor)
                        print(f"Você sacou R$ {valor} da sua conta, seu saldo atual é de R$ {conta.saldo}")
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")
        
        if funcao == 4:
            titular = input("Informe o nome do titular da conta que deseja depositar:")
            valor = float(input("Informe o valor que deseja depositar:"))
            for conta in banco:
                if conta.titular == titular:
                    conta.depositar(valor)
                    print(f"Você depositou R$ {valor} na sua conta, seu saldo atual é de R$ {conta.saldo}")
                    conta.saldo += valor
            else:
                resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                if resposta == "s":
                    break
                else:
                    print("Programa encerrado!")
        
        if funcao == 5:
            titular = input("Informe o nome do titular da conta que deseja transferir:")
            valor = float(input("Informe o valor que deseja transferir:"))
            destinatario = input("Informe o nome do destinatário:")
            for conta in banco:
                if conta.titular == titular:
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
                        resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                        if resposta == "s":
                            break
                        else:
                            print("Programa encerrado!")
        if funcao == 6:
            titular = input("Informe o nome do titular da conta que deseja ver o histórico:")
            for conta in banco:
                if conta.titular == titular:
                    print(f"Historico de {conta.titular}:")
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
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")

        if funcao == 7:
            titular = input("Informe o nome do titular da conta que deseja excluir:")
            for conta in banco:
                if conta.titular == titular:
                    banco.remove(conta)
                    print(f"Conta de {titular} excluída com sucesso!")
                else:
                    resposta = input("Conta não encontrada! Deseja consultar novamente? s/n")
                    if resposta == "s":
                        break
                    else:
                        print("Programa encerrado!")
                    

    if funcao == 8:
        print("Sistema encerrado!")
        break




        
        

    


