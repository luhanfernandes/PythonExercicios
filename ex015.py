nome = (input('Olá! digite seu nome: '))

print(f'Olá, {nome}! Seja bem vindo!')
dias = int(input('Por quantos dias o carro foi alugado: '))
uso = float(input('Por quantos KM o carro foi utilizado: '))

total = (60 * dias) + (0.15 * uso)

print(f'O total a ser pago é R$ {total}')