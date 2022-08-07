idade = 0
ida = 0
maior = 0
homem = ''
mulher = 0

for c in range(1,5):
    print(f'----- {c}° PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo: ')).strip().title()

    if sexo == 'M':
        idade = int(input('Idade: '))
        ida = ida + idade
        if idade > maior:
            maior = idade
            homem = nome
    elif sexo == 'F':
            idade = int(input('Idade: '))
            ida = ida + idade
            if 21 > idade:
                mulher += 1



print(f'A média de idade é: {ida / 4} anos!')
print(f'O {homem} é o mais velho e tem: {maior} anos!')
print(f'O total de mulheres com menos de 21 anos é: {mulher}')