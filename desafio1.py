menu = """

["d"] Depositar
["s"] Sacar
["e"] Extrato
["q"] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_operacao = 1

while True:

    opcao = input(menu)
    
    if opcao == "d":
        txt = "DEPÓSITO"
        print(txt.center(87,"-"))
        deposito = float(input("\nDigite o valor que deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"\nOperação número {numero_operacao}: Foi feito um depósito de R${deposito:.2f}, seu saldo atual é de R${saldo:.2f}."
            numero_operacao += 1
            print(f"\nDepósito de R${deposito:.2f} concluído com sucesso.")
        else:
            print("Valor inválido, tente novamente.")    
        
        
        
    elif opcao == "s":
        txt = "SAQUE"
        print(txt.center(88,"-"))
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("\nDigite o valor que deseja sacar: "))
            if saque > 0 and saque <= saldo and saque <= limite:
                saldo -= saque
                extrato += f"\nOperação número {numero_operacao}: Foi feito um saque de R${deposito:.2f}, seu saldo atual é de R${saldo:.2f}."
                print(f"\nSaque de R${saque:.2f} concluído com sucesso.")
                numero_saques += 1
                numero_operacao += 1
            elif saque > limite:
                print("\nVocê não pode sacar um valor maior que o seu limite por transação.")
            elif (saque > 0 and saque > saldo):
                print("\nVocê não pode sacar um valor maior que o seu saldo.")    
            else:
                print("\nValor inválido, tente novamente.")            
        else:
            print("Você já atingiu o limite de saques diário.")
            numero_saques = 0

    elif opcao == "e":
        txt = "EXTRATO"
        print(txt.center(87,"="))
        print(f"\nÚltimas operações:\n {extrato}")
        print("=======================================================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione outra opção.")
