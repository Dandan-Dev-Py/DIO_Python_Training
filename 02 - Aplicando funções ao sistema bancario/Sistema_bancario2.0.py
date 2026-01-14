menu = """
[cu] Criar Usuario
[cc] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500


def criar_usuario(usuarios):
    cpf = input("Qual o CPF? (apenas numeros): ")
    

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com este CPF! ")
            return

    nome = input("Qual o nome do usuario?: ")
    data_nascimento = input("Qual a data de nascimento? (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    
    
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_encontrado}
    
    print("\n Usuário não encontrado! Crie o usuário primeiro. ")
    return None

def deposito(saldo, extrato, /):
    valor = float(input("Qual o valor do depósito?: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado! ")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Qual o valor do saque?: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" Saldo insuficiente! ")
    elif excedeu_limite:
        print(f" O limite por saque é de R$ {limite} ")
    elif excedeu_saques:
        print(" Limite diário de saques atingido! ")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(" Saque realizado com sucesso! ")
    else:
        print(" Valor inválido! ")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")


while True:
    opcao = input(menu).lower()

    if opcao == "cu":
        criar_usuario(usuarios)

    elif opcao == "cc":
        numero_conta = len(contas) + 1
        conta = criar_conta("0001", numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            extrato=extrato,
            limite=LIMITE_VALOR_SAQUE,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

