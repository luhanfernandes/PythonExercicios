num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior que o segundo!')
elif num2 > num1:
    print('O segundo valor é maior que o primeiro!')
else:
    print('Não existe valor maior, os dois são iguais')