

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito = float(input("Informe um valor para depósito: "))

        if valor_deposito > 0:

            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "s":

        print("Saque")

        valor_saque = int(input("Informe um valor para sacar: "))

        if numero_saques >= LIMITE_SAQUES:
            print("Operação inválida! Você atingiu o limite de diário de saques.")
        if valor_saque > limite:
            print("Operação inválida. O valor limite por saque foi atingido!")
        if valor_saque > saldo:
            print("Operação inválida. Saldo insuficiente!")

        if valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "e":

        print("Extrato")
        print("Sem movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Escolha novamente a operação desejada.")
