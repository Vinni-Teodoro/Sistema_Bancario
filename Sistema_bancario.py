Menu = '''

[1] = Depositar
[2] = Saque
[3] = Extrato
[0] = Sair

=> '''

Saldo = 0
Limite = 500
Extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUE = 3

while True:

    opcao = input(f"Seleione a opção desejada:{Menu}" )

    if opcao == "1":
        deposito = float(input("Digite o valor do deposito:"))

        if deposito > 0:
            Saldo += deposito
            Extrato += f'Deposito: R$ {deposito: .2f}\n'

        else:
            print("Operação cancelada! Valor digitado incorreto.")
                

    elif opcao == "2":
        saque= float(input("Digite o valor que deseja sacar: "))

        saque_maior = saque > Saldo
        saque_maior_limite = saque > Limite
        excedeu_numero_de_saque = numero_de_saques > LIMITE_DE_SAQUE        

        if saque_maior:
            print("Você não tem saldo disponível")

        elif saque_maior_limite:
            print("Seu limite de saque é R$ 500,00")

        elif excedeu_numero_de_saque:
            print("Seu limite diário de saque já foi feito.")

        elif saque > 0:
            Saldo -= saque
            Extrato += f'Saque R$ {saque:.2f}\n'
            numero_de_saques += 1

        else:
            print("Operação cancelada.")           


    elif opcao == "3":
        print("------------------EXTRATO--------------")
        print("Não foram realizadas transações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo: .2f}")
        print("Obrigado por utilziar os nossos serviços. :)")
        print("---------------------------------------")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada.")          