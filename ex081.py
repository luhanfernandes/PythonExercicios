lista = []
cont = 0

while True:
    lista.append(int(input('Digite um valor para ingressar na lista: ')))
    cont += 1
    seguir = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if seguir == 'N':
        break
    while seguir not in 'NS':
        seguir = str(input('Opção invalida. Deseja continuar?: [S/N] ')).upper().strip()[0]
        break

lista.sort(reverse=True)
print(f'A lista na ordem inversa ficou: {lista}')

if 5 in lista:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não está na lista!')
