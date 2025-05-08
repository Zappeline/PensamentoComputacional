from models.contas import Contas

banco = []

print("Sistema Bancário")

while True:
    funcao = int(input("Menu bancario, digite a ação que deseja efetuar:\n" \
                "1- Criar conta\n2- Exibir saldo\n3- Sacar\n4-Depositar\n" \
                "5- Realizar transferencia\n6- Exibir historico\n7- Excluir conta\n"
                "8- Sair\n"
                "Informe a opção:"))

    if funcao > 0 and funcao < 8:
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
                    r = input("Conta não encontrada! Deseja consultar novamente? s/n")
                    if r == "s":
                        break
                    else:
                        print("Programa encerrado!")

        if funcao == 8:
                print("Programa encerrado!")
                break   





        
        

    


