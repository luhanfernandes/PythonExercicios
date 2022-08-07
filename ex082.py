lista = []
lista_par =  []
lista_impar = []

 
while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if cont == 'N':
        break

    while cont not in 'SN':
        cont = str(input('Opção Invalida. Deseja continuar? [S/N]: ')).upper().strip()[0]

print(f'A lista completa é: {lista}')
print(f'A lista PAR é: {lista_par}')
print(f'A lista IMPAR é: {lista_impar}')

