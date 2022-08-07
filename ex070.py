#variaveis
total = 0
maismil = 0
baratonome = ''
baratopreco = 0
continuar = ''
teste = 0

while True:
    nome = str(input('\nNome do produto: ')).title().strip()
    preco = int(input('Valor: R$ '))

    total += preco

    if preco > 1000:
        maismil += 1

    if teste == 0:
        baratopreco = preco
        baratonome = nome

    if preco < baratopreco:
        baratonome = nome

    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        print('Fim do programa!')
        break 

print(f'\nVocê gastou no total: R$ {total}')
print(f'{maismil} produtos custaram mais de R$ 1000')
print(f'{baratonome} foi o produto mais barato que você comprou hoje!')