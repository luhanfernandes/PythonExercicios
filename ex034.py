salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario = (salario * 110) / 100
    print(f'Seu novo salário é: R${salario} reais!')
else:
    salario = (salario * 115) / 100
    print(f'Seu novo salário é: R${salario}!')