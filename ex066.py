#Variaveis
num = 0
soma = 0
cont = 0

while num != 999:

    num = int(input('Digite um valor: '))

    if num == 999:
        break

    cont += 1
    soma += num


print(f'Você digitou {cont} numeros e a soma deles é: {soma}')