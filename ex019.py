import random

'''num = random.randint(1,4)

nome1 = input('Digite o nome do 1° aluno: ')
nome2 = input('Digite o nome do 2° aluno: ')
nome3 = input('Digite o nome do 3° aluno: ')
nome4= input('Digite o nome do 4° aluno: ')
num1 = input('Digite o número do 1° aluno: ')
num2 = input('Digite o número do 2° aluno: ')
num3 = input('Digite o número do 3° aluno: ')
num4 = input('Digite o número do 4° aluno: ')

print(f'O número escolhido foi: {num}')

if num == 1:
    print(f'O aluno escolhido foi: {nome1}')
elif num == 2:
    print(f'O aluno escolhido foi: {nome2}')
elif num == 3:
    print(f'O aluno escolhio foi: {nome3}')
else:
    print(f'O aluno escolhido foi: {nome4}')'''''


alu1 = input('Digite o nome do primeiro aluno: ')
alu2 = input('Digite o nome do segundo aluno: ')
alu3 = input('Digite o nome do terceiro aluno: ')
alu4 = input('Digite o nome do quarto aluno: ')

lista = [alu1, alu2, alu3, alu4]

escolhido = random.choice(lista)
print(f'O aluno {escolhido} foi selecionado!')