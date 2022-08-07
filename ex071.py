valor50 = 0
valor20 = 0
valor10 = 0
valor1 = 0

print('=' * 30)
print('{:^50}'.format('Banco do sem dinheiro'))
print('=' * 30)

num = int(input('Que valor sacar: '))

valor50 = num // 50 #valor50 vai receber a divisão inteira do numero por 50 (quantidade de notas)

if num % 50 != 0: #Se o resto da divisão do numero por 50 for diferente de 0, ou seja, sobrar
    num = num % 50 #Numero vai receber o resto da divisão entre numero e 50

    valor20 = num // 20 #valor20 vai receber a divisão inteira do numero por 20 (quantidade de notas)
    if num % 20 != 0: #se o resto da divisão do numero por 20 for diferente de zero, ou seja, sobrar
        num = num % 20 #Numero vai receber o resto da divisão entre numero e 20

        valor10 = num // 10#valor10 vai receber a divisão inteira do numero por 10 (quantidade de notas)
        if num > 0: #se o que restou do numero ainda for maior que zero
            num = num % 10 #numero vai receber o resto da divisão de numero por 10
            valor1 = num // 1 #valor1 vai receber a divisão inteira do numero por 1 (quantidade de notas)


print(f'Total de {valor50} cédulas de R$ 50')
print(f'Total de {valor20} cédulas de R$ 20')
print(f'Total de {valor10} cédulas de R$ 10')
print(f'Total de {valor1} cédulas de R$ 1')