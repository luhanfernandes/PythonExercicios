print('='*30)
print('Cadastramento de pessoas')
print('=' * 30)

conti = 0
conts = 0
contm = 0
continuar = ''

while True:

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade > 18:
        conti += 1
    if sexo == 'M':
        conts += 1
    if sexo == 'F' and idade < 20:
        contm += 1

    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    while continuar != 'S' and continuar != 'N': #while tipo not in 'SN':
        continuar = str(input('Deseja continua1r [S/N]: '))

    if continuar == 'N':
        break

print(f'\nO total de pessoas maiores de 18 anos foi de: {conti}')
print(f'O total de homens cadastrados foi de: {conts}')
print(f'O total de mulheres abaixo de 20 anos foi de: {contm}')