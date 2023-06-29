import textwrap

def menu():
    titulo = '\n{:*^100}'.format(' TDG BANK ')  
    menu = """
    [1] Depósito 
    [2] Saque 
    [3] Extrato 
    [4] Cadastro de Clientes
    [5] Cadastro de Conta Corrente
    [6] Lista Contas Correntes Cliente
    [7] Sair
    """
    print(titulo, menu,'\n{:*^100}'.format(''))
    return input('  >> Informe a opção desejada: ')


def sacar(*, qtd_saque_dia, valor_limite_saque, saldo_atual, valor_limite_diario, list_extrato):

    print('\n{:*^60}'.format(' SAQUE '))
    if qtd_saque_dia == 0:
        print('\n  >> Oops!  Limite de 03 saques diários excedido!!')

    else:
        while True:
            try:
                valor = float(
                    input('\n  >> Informe o  valor a ser sacado: ').replace('-', ''))

                if valor > valor_limite_saque:
                    print(
                        f'\n  >> Oops!  Limite diário de R$ {valor_limite_diario:.2f} para saques excedido!!')
                    break

                elif valor <= saldo_atual:
                    saldo_atual -= valor
                    list_extrato.append(('Saque: ', valor * -1))
                    qtd_saque_dia -= 1
                    valor_limite_saque -= valor
                    print(
                        f'\n  >> ===== Saque no valor de R$ {valor:.2f} realizado com sucesso!! ====='
                        )
                    break
                else:
                    print('\n  >> Oops!  Saldo insuficiente!!  Tente Novamente...')

            except ValueError:
                print('\n  >> Oops!  Valor Inválido!!  Tente Novamente...')

    return qtd_saque_dia, valor_limite_saque, saldo_atual, list_extrato


def depositar(saldo_atual, list_extrato, /):

    print('\n{:*^60}'.format(' DEPÓSITO '))
    while True:
        try:
            valor = float(input('  >> Informe o  valor a ser depositado: '))
            if valor >= 0:
                saldo_atual += valor
                list_extrato.append(('Depósito: ', valor))
                print(f'\n  >> !!!! Valor de R$ {valor:.2f} depositado com sucesso!!!!')
                break
            else:
                print(
                    '\n  >> Oops!  Valor Inválido!!  Depósito somente em valores positivos. Tente Novamente...')

        except ValueError:
            print(
                '\n  >> Oops!  Valor Inválido!!  Depósito somente em valores inteiros. Tente Novamente...')

    return saldo_atual, list_extrato


def exibir_extrato(saldo, /, *, list_extrato):
    print('\n{:*^60}'.format(' EXTRATO '),)
    for tipo, valor in list_extrato:
        print(f'  >> {tipo.upper():>10} R$ {valor:.2f}')
    print('\n{:*^60}'.format(''),)
    print(f'\n  >> SALDO ATUAL R$ {saldo:.2f}')


def criar_usuario(lista_conta_user):
    print('\n{:*^60}'.format(' CADASTRO DE NOVOS CLIENTES '),)
    while True:
        try:
            cpf = int(
                input('\n  >> Informe o CPF do novo cliente ou "0" para sair: '))
            if cpf == 0:
                break

            elif cpf in lista_conta_user:
                print('  >> Oops!  Cliente já cadastrado!! Tente Novamente...')

            else:
                nome = input('  >> Informe o nome do novo cliente: ')
                dt_nasc = input(
                    '  >> Informe a data de nascimento (dd/mm/aa) do novo cliente: ')
                end = input('  >> Informe o endereço completo do novo cliente: ')

                lista_conta_user[cpf] = {'nome': nome,
                                       'dt_nasc': dt_nasc, 'end': end}
                print(f'\n  >> ===== Cliente {nome.upper()} cadastrado com sucesso!! =====')
                
                return lista_conta_user

        except ValueError:
            print('\n  >> Oops!  Valor Inválido!!  CPF somente números. Tente Novamente...')


def criar_conta(AGENCIA, lista_contas, lista_conta_user): 
    print('\n{:*^60}'.format(' CADASTRO DE CONTAS CORRENTES '),)
    while True:
        try:
            cpf = int(input('  >> Informe o CPF do cliente: '))
            if cpf in lista_conta_user:
                lista_contas.append({'CPF':cpf
                                     ,'conta':len(lista_contas)+1
                                     ,'agencia':AGENCIA}
                                    )
                print('\n  >> ===== Conta Corrente cadastrada!! =====')
                print(f'\n      >> Agência: {AGENCIA:5}   Conta Corrente: {len(lista_contas)}\n')
                return lista_contas

            else:
                print('\n  >> Oops!  Cliente não cadastrado!!')
                return lista_contas
            
        except ValueError:
            print('\n  >> Oops!  Valor Inválido!!  CPF somente números. Tente Novamente...')


def exibir_contas(lista_contas, lista_user):
    while True:
        try:
            cpf_user = int(input('\n  >> Informe o CPF do cliente ou "0" para sair: '))
            if cpf_user == 0:
                return
            
            elif cpf_user not in lista_user:
                print('  >> Oops!  Cliente NÃO cadastrado!! Tente Novamente...')
                                    
            else:
                print('\n{:*^60}'.format(' LISTA DE CONTAS CORRENTES: '),)     
                print(f"  >> CLIENTE: {lista_user[cpf_user]['nome']:5} CPF: {cpf_user}")         
                if not [usuario for usuario in lista_contas if usuario['CPF'] == cpf_user]:
                    print('      >> Oops!  Cliente SEM conta corrente cadastrada!!')
                else:
                    for conta in lista_contas:
                        if conta['CPF'] == cpf_user:
                            print(f"      >> Agência: {conta['agencia']:5} Conta Corrente: {conta['conta']}")
                print('{:*^60}'.format(''),)
                return

        except ValueError:
            print('\n  >> Oops!  Valor Inválido!!  CPF somente números. Tente Novamente...')
    

saldo = 0
LIMITE_SAQUE = 500
limite_diario = LIMITE_SAQUE
saques_diario = 3
extrato = []
lista_clientes = {}
lista_contas = []
AGENCIA = '001'

while True:    
    opcao = menu()

    if opcao == '1':
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == '2':
        saques_diario, limite_diario, saldo, extrato = sacar(
            qtd_saque_dia=saques_diario
           ,valor_limite_saque=limite_diario
           ,saldo_atual=saldo
           ,valor_limite_diario=LIMITE_SAQUE
           ,list_extrato=extrato
        )

    elif opcao == '3':
        exibir_extrato(saldo, list_extrato=extrato)

    elif opcao == '4':
        lista_clientes = criar_usuario(lista_clientes)

    elif opcao == '5':
        lista_contas = criar_conta(AGENCIA, lista_contas, lista_clientes)

    elif opcao == '6':
        exibir_contas(lista_contas, lista_clientes)

    elif opcao == '7':
        print('\n  >> !!! Obrigado por ser um cliente TDG BANK !!!')
        break

    else:
        print('Opção inválida!!')
