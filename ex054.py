from datetime import date

atual = date.today().year
acima = 0
abaixo = 0

for c in range(0,7):
    ano = int(input('Qual ano você nasceu?: '))
    idade = atual - ano

    if idade >= 21:
        acima += 1
    elif idade < 21:
        abaixo += 1

print(f'Temos {acima} maiores de 21 anos! e {abaixo} menores de 21!')


