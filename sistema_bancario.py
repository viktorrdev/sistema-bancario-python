

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor a depositar: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Digite um número positivo!")

    elif opcao == "2":
        valor = float(input("Digite o valor a sacar: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! O número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Digite um número positivo.")

    elif opcao == "3":
        print("\n=========== EXTRATO ============")
        print("Nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "4":
        print("Saindo do sistema... Até Logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")


