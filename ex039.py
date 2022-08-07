from datetime import date
import time

"""dia_nasc = int(input('Digite o dia do seu nascimento: '))
mes_nasc = int(input('Digite o mes do seu nascimento: '))
ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = (time.localtime().tm_year)
idade = int((time.localtime().tm_year) - ano_nasc)
dia_res = (time.localtime().tm_mday) - dia_nasc
mes_res = (time.localtime().tm_mon) - mes_nasc

if ano_atual - ano_nasc < 18:
    print('Você ainda vai se alistar no exercito!')
    print(f'Faltam {dia_res} dias, {mes_res} meses e {18 - idade} ano(s) para seu alistamento!')
elif ano_atual - ano_nasc == 18:
    print('Está na hora de realizar seu alistamento!')
elif ano_atual - ano_nasc > 18:
    print('Já passou da hora de se alistar!')"""


atual = date.today().year
sexo = str(input('Qual seu sexo?: ')).title()


if sexo == 'Masculino':

    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc

    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

    if idade == 18:
        print(f'Você tem que se alistar esse ano!')
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print(f'Você ainda não tem 18 anos. Faltam {saldo} anos para o alistamento!')
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print(f'Você já deveria ter se alistado a {saldo} anos!')
        print(f'Seu alistamento foi em {ano}')

else:
    print('Você não precisa se alistar!')