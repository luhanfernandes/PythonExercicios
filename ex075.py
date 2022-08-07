num = ((int(input('Digite um valor: '))), (int(input('Digite outro valor: '))),
       (int(input('Digite outro valor: '))), (int(input('Digite outro valor: '))))

print(f'O número 9 apareceu {num.count(9)} vezes!')

if num.count(3) > 0:
    print(f'O número 3 apareceu pela primeira vez na posição {num.index(3)+1}')
else:
    print('O número 3 não apareceu!')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
