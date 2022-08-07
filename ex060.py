'''from math import factorial

n = factorial(5)
print(n)'''


n = int(input('Digite um valor: '))
c = n
f = 1
print(f'Calculando {n}!')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end= ' ')
    f = f * c
    c -= 1
print(f)