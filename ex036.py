#Programa para aprovar um emprestimo de casa, valor, salario, tempo, maximo 30% do salario

casa = float(input('Qual o valor da casa?: R$ '))
salario = float(input('Qual o seu salário?: R$ '))
anos = int(input('Em quantos anos você pagará a casa?: '))
meses = anos * 12
prestacao = casa / meses

print(f'Para pagar uma casa de {casa} em {anos} anos a prestação será de {prestacao:.2f}!')

if prestacao > (salario * 30) / 100:
    print('Seu empréstimo foi negado!')
elif prestacao < (salario * 30) / 100:
    print('Seu empréstimo foi aceito!')