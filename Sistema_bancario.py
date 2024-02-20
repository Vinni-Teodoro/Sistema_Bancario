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
        print("Saque")

    elif opcao == "3":
        print("Extrato")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada.")          