#desafio do sistema bancário bootcamp DIO - atualizando o sistema com funções, incluindo as novas funções criar_usuario e criar_conta

from datetime import date, datetime, timedelta

def menu():
    menu = """
    ______________MENU______________    
    [u] Criar novo usuário
    [c] Criar nova conta
    [d] Depositar
    [s] Sacar
    [e] Exibir extrato
    [l] Listar contas 
    [q] Sair

    => """

    return input(menu)

def depositar(saldo, valor, extrato, operacao_por_dia, /):
    txt = "DEPÓSITO"
    print(txt.center(107,"-"))
    if valor > 0:
        saldo += valor
        extrato += f"\nOperação número {operacao_por_dia} - Depósito de R${valor:.2f}."
        operacao_por_dia += 1
        print(f"\nDepósito de R${valor:.2f} concluído com sucesso.")
    else:
        print("Valor inválido, tente novamente.")  

    return saldo, extrato, operacao_por_dia

def sacar(*,saldo, valor, extrato, limite, limite_saques, numero_saques, operacao_por_dia):
    txt = "SAQUE"
    print(txt.center(108,"-"))
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite 
    saques_excedidos = numero_saques >= limite_saques
    if saques_excedidos:
        print("Falha na operação: você já atingiu o limite de saques diário.")
    elif limite_excedido:
        print("\nFalha na operação: você não pode sacar um valor maior que o seu limite por transação.")
    elif saldo_excedido:
        print("\nFalha na operação: você não pode sacar um valor maior que o seu saldo.") 
    elif valor > 0:
        saldo -= valor
        extrato += f"\nOperação número {operacao_por_dia} - Saque de R${valor:.2f}."
        operacao_por_dia += 1
        print(f"\nSaque de R${valor:.2f} concluído com sucesso.")
        numero_saques += 1
    else:
        print("Falha na operação: valor inválido, tente novamente.")  

    return saldo, extrato, numero_saques, operacao_por_dia


def exibir_extrato(saldo, /, *, extrato):
    txt = "EXTRATO"
    extrato += (f"\nSeu saldo atual é de R${saldo:.2f}.\n")
    print(txt.center(107,"="))
    print(f"\n {extrato}")
    print("===========================================================================================================")
    return extrato

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF: ")
    cpf = "".join(filter(str.isalnum,cpf))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nEste CPF já está cadastrado.")
    else:
        nome = input("Insira o nome completo: ")
        data_nascimento = input("Insira a data de nascimento (dd/mm/aa): ")
        endereco = input("Informe o endereço (rua, número, bairro, cidade/sigla estado): ")
        usuarios.append({"nome": nome, "cpf":cpf, "data_nascimento":data_nascimento, "endereco":endereco})
        print("\nUsuário criado com sucesso!")
        
def filtrar_usuario(cpf,usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuario_filtrado[0] if usuario_filtrado else None
      
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, cadastre o usuário primeiro.")

def consultar_contas(contas):
    for conta in contas:
        consulta = f"""Agência: {conta["agencia"]}\nNº da conta: {conta["numero_conta"]}\nTitular: {conta["usuario"]["nome"]}
                    """
        print("===========================================================================================================")
        print(consulta)
        print("===========================================================================================================")

def main():
    
    saldo = 0
    limite = 500
    extrato = ""

    numero_saques = 0
    LIMITE_SAQUES = 3
    
    operacao_por_dia = 1
   
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "d":
            valor = float(input("\nDigite o valor que deseja depositar: "))
            saldo, extrato, operacao_por_dia = depositar(saldo, valor, extrato, operacao_por_dia)
                                      

        elif opcao == "s":
            valor = float(input("\nDigite o valor que deseja sacar: "))    
            saldo, extrato, numero_saques, operacao_por_dia = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques,
                operacao_por_dia=operacao_por_dia,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "l":
            consultar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione outra opção.")
 
main()