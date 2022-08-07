a = float(input('Digite um tamanho: '))
b = float(input('Digite outro tamanho: '))
c = float(input('Digite mais um tamanho: '))

if (b-c) < a < b + c and (a-c) < b < a +c and (a-b) < c < a + b:
    print('\33[1;35;41mSeu triangulo existe!\33[m')
else:
    print('\33[1;32;42mSeu triangulo não pode ser formado!\33[1;37;42m')

