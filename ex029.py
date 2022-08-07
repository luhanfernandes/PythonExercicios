vel = float(input('Qual a velocidade do carro em KM/H?: '))
multa = (vel - 80) * 7

if vel > 80:
    print(f'Você vai pagar uma multa de R$ {multa} reais!')
else:
    print('Parabéns, você esta na velocidade certa!')