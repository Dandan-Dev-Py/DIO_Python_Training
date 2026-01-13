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
conta = []

while True:

    opcao = input(menu)

#cara, dá uma olhada pra ver se a conta ta vinculada ao usuario,tipo se ela ta atrelada por cpf
    def criar_usuario(usuarios=usuarios):

        nome = input("Qual o nome do usuario?: ")
        data_nascimento = input("Qual a data de nascimento do usuario? : ")
        cpf = input("Qual o CPF? (apenas numeros): ")
        endereco = input("Qual o endereco? (logradouro, numero - bairro - cidade/sigla estado): ")

        for usuario in usuarios:
            if cpf == usuario["cpf"]:
                print("Este usuario ja existe")
                return


    def criar_conta(conta=conta, usuarios=usuarios):

        agencia = "0001"
        usuario = input("digite o cpf do usuario?: ") 
        numero_conta = len(conta) + 1

        if usuario not in usuarios:
            print("Usuario não encontrado, por favor crie um usuario antes de criar uma conta")
            return

        conta.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})    
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("usuario cadastrado")


    def deposito(saldo, transação, extrato):
        saldo = saldo
        extrato = extrato
        transação = int(input("Qual o valor desejado?: "))
        if transação > 0:
            saldo += transação
            extrato += str(f"deposito = R${transação}\n")
            return saldo, extrato 

        else:
            print("não é possivel adicionar um valor menor ou equivalente a 0")    
                

    def saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=500, LIMITE_SAQUES=3):

        transação = int(input("Qual o valor desejado?: "))

        if transação <= saldo and transação <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= transação
            numero_saques += 1

            extrato += str(f"Saque = R${transação} \n")
            return saldo, extrato


        elif numero_saques >= LIMITE_SAQUES:
            print("Numero maximo de saques atingido")
        elif transação > saldo:
            print("Saldo insuficiente")  
        elif transação > limite:
            print("o limite de saque é 500 reais")          


    def Extrato(saldo, extrato=extrato):
      
        if extrato != "":
            return f'Extrato = {extrato} \n \n Saldo restante = {saldo}'
        if extrato == "":
            return f"não foram realizadas movimentações \n \n Saldo restante = {saldo}"


    if opcao == "cu":
        criar_usuario()

    if opcao == "cc":
        criar_conta()    
    if opcao == "s":
        saque()

    if opcao == "d":
        deposito()
    
    if opcao == "e":
        Extrato()
    
    if opcao == "q":
       print("Obrigado por usar nosso sistema bancario") 
       break
