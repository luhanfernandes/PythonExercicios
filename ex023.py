#Leia de 0 a 9999 e mostrecada um dos digitos separados

#Quebrando o número

"""num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)
#Evideniando o número

if num <= 9:
    print(f'unidade: {n[0]}')

elif num <= 99:
    print(f'unidade: {n[1]}')
    print(f'dezena: {n[0]}')

elif num <= 999:
    print(f'unidade: {n[2]}')
    print(f'dezena: {n[1]}')
    print(f'centena: {n[0]}')

elif num <= 9999:
    print(f'unidade: {n[3]}')
    print(f'dezena: {n[2]}')
    print(f'centena: {n[1]}')
    print(f'milhar: {n[0]}')

else:
    print('Número invalido!')"""



num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

