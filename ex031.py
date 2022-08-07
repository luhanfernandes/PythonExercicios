distancia = float(input('Qual a distância da viagem?: '))

if distancia <= 200:
    print(f'Você vai pagar R$ {distancia * 0.50} reais!')
else:
    print(f'Você vai pagar R$ {distancia * 0.45} reais!')