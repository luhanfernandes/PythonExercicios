while True:

    num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    op = int(input('Digite um número entre 0 e 20: '))
    while op < 0 or op > 20:
        op = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {num[op]}')