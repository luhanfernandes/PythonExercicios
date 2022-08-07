from datetime import date

ano = int(input('Qual ano você quer verificar? 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É ano bissexto!')
else:
    print('Não é!')
