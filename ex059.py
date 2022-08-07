menu = 0
op = 0

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

while op !=5:

    op = int(input('''\nSELECIONE A OPERAÇÃO
        [ 1 ] - Somar
        [ 2 ] - Multipliacar
        [ 3 ] - Maior
        [ 4 ] - Novos números
        [ 5 ] - Sair do progama
        Sua escolha: '''))

    if op == 1:
        soma = (n1 + n2)
        print(f'A soma entre {n1} e {n2} é: {soma}')
    elif op == 2:
        multi = (n1 * n2)
        print(f'A multiplicação de {n1} e {n2} é: {multi}')
    elif op == 3:
        if n1 > n2:
            print(f'O {n1} é maior que o {n2}!')
        elif n2 > n1:
            print(f'O {n2} é maior que o {n1}')
        else:
            print(f'{n1} e {n2} são iguais!')
    elif op == 4:
        n1 = float(input('Escolha um novo número: '))
        n2 = float(input('Escola um outro número: '))

    elif op == 5:
        break
    else:
        print('Opção inválida!')


