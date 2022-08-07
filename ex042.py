r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo!')

    if r1 == r2 and r1 == r3:
        print('É um triangulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triangulo ISÓSCELES!')
    else:
        print('É um triangulo ESCALENO!')

else:
    print('Não podem formar um triangulo!')