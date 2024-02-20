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
        valor = float(input("Digite o valor do deposito:"))

        if valor > 0:
            Saldo += valor
            Extrato += f'Deposito: R$ {valor: .2f}\n'

        else:
            print("Operação cancelada! Valor digitado incorreto.")
                

    elif opcao == "2":
        valor = float(input("Digite o valor de Saque"))

        saque_maior = valor > Saldo

        saque_maior_limite = valor > Limite

        excedeu_saque = numero_de_saques > LIMITE_DE_SAQUE

        if saque_maior:
            print("Valor digitado, maior que seu saldo!")

        elif saque_maior_limite:
            print("Valor digitado, maior que o limite diário!")

        elif excedeu_saque:
            print("Limite de saque diário atingido, operação cancelada!")  

        elif valor > 0:
            Saldo += valor
            Extrato += f'Saque: R$ {valor: .2f}\n'
            numero_de_saques += 1

        else:
            print("Operação cancelada! Valor digitado incorreto.")          


    elif opcao == "3":
        print("------------------EXTRATO--------------")
        print("Não foram realizadas transações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo: .2f}")
        print("---------------------------------------")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada.")          