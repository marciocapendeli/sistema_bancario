

# Variáveis do sistema
saldo = 0.0
depositos = []
saques = []
LIMITE_SAQUES = 3
VALOR_MAX_SAQUE = 500.0
quantidade_saques = 0

# Funções
def mostrar_menu():
    print("\n==============================")
    print("Bem-vindo ao Banco Python!")
    print("Selecione a operação desejada:")
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[0] Sair")
    print("==============================")

def depositar(valor):
    global saldo, depositos
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, saques, quantidade_saques
    if quantidade_saques >= LIMITE_SAQUES:
        print("Erro: Limite diário de saques atingido (3 saques por dia).")
    elif valor > VALOR_MAX_SAQUE:
        print(f"Erro: O valor do saque não pode exceder R$ {VALOR_MAX_SAQUE:.2f}.")
    elif valor > saldo:
        print("Erro: Saldo insuficiente para saque.")
    elif valor <= 0:
        print("Erro: O valor do saque deve ser positivo.")
    else:
        saldo -= valor
        saques.append(valor)
        quantidade_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def mostrar_extrato():
    print("\n========= EXTRATO =========")
    if not depositos and not saques:
        print("Nenhuma movimentação realizada.")
    else:
        if depositos:
            print("Depósitos:")
            for d in depositos:
                print(f"  R$ {d:.2f}")
        if saques:
            print("Saques:")
            for s in saques:
                print(f"  R$ {s:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("============================\n")

# Loop principal do sistema
while True:
    mostrar_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        except ValueError:
            print("Erro: Informe um número válido.")
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor)
        except ValueError:
            print("Erro: Informe um número válido.")
    elif opcao == "3":
        mostrar_extrato()
    elif opcao == "0":
        print("Obrigado por usar o Banco Python. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")


#obrigado pelas aulas!