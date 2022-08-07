from math import hypot

'''oposto = float(input('Qual o comprimento do cateto oposto: '))
adjacente = float(input('Qual o comprimento do cateto adjacente: '))
hi = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai valer: {hi:.2f}!')'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print(f'A hipoteusa vai valer: {hi:.2f}!')