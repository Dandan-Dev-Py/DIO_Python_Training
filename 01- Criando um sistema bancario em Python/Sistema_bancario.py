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
        deposito = float(input("quanto deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            extrato += str(f"Deposito = R${deposito} \n")
        else:
            print('Não é possivel adicionar um valor menor que 0')



    if opcao == "s":
        saque = float(input("quanto deseja sacar? "))
        if saque <= saldo and saque <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= saque
            numero_saques += 1

            extrato += str(f"Saque = R${saque} \n")
        elif numero_saques >= LIMITE_SAQUES:
            print("Numero maximo de saques atingido")
        elif saque > saldo:
            print("Saldo insuficiente")  
        elif saque > limite:
            print("o limite de saque é 500 reais")          


    if opcao == "e":
        if extrato != "":
            print(f'Extrato = {extrato} \n \n Saldo restante = {saldo}')
        if extrato == "":
            print(f"não foram realizadas movimentações \n \n Saldo restante = {saldo}")
    
    if opcao == "q":
       print(p)
