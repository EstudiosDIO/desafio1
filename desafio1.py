menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Selecione a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Valor inválido")

    elif opcao == 2:
        valor = float(input("Informe o valor que deseja sacar:"))

        excedeu_diario = numero_saques >= LIMITE_SAQUES

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        if excedeu_diario:
            print("Numero de saques diário excedido.")

        elif excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("Excedeu seu limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Valor de saque inválido!")

    elif opcao == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == 0:
        break

    else:
        print("Opção Inválida")
