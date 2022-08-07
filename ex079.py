valores = []

while True:
    num = int(input('Digite um valor para integrar a lista: '))
    if num not in valores:
        valores.append(num)
        print('Digito aceito!')
        cont = str(input('Desejar continuar? [S/N]: ')).title().strip()[0]
    else:
        print('Valor já computado, não pode ser aceito!')
        cont = str(input('Deseja continuar? [S/N]: '))

    if cont == 'N':
        break

    while cont not in 'SN':
        cont = str(input('Opção Invalida. Desejar continuar? [S/N]: ')).title().strip()[0]

print(f'Você digitou os valores: {sorted(valores)}')


