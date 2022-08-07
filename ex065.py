continuar = ''
cont = 0
soma = 0
maior = 0
menor = 10000

while continuar != 'N':
    num = int(input('Digite um valor: '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'A média entre todos os números digitados foi: {soma / cont}')
print(f'O maior número digitado foi: {maior} e o menor foi {menor}')