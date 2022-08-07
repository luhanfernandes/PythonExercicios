n = 0
c = 0
soma = 0

while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma = soma + n
        c += 1
    else:
        print('Programa encerrado.')

print(f'A soma total foi de {soma} e a quantidade de números digitados foram {c}')


