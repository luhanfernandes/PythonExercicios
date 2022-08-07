import datetime
import time

ano_nasc = int(input('Digite o ano do nascimento: '))
idade = (datetime.date.today().year - ano_nasc)

if idade <= 9:
    print(f'Você tem {idade} anos e é MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e é INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e é JUNIOR!')
elif idade == 20:
    print(f'Você tem {idade} e é SÊNIOR!')
else:
    print(f'Você tem {idade} e é MASTER!')