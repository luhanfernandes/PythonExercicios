preco = float(input('Digite o preço do produto: '))
pagamento = int(input('[ 1 ] - Dinheiro / Cheque \n[ 2 ] - A vista no cartão \n[ 3 ] - 2x no cartão \n[ 4 ] - 3x ou mais no cartão\n'))

if pagamento == 1:
    preco = (preco * 90) / 100
    print(f'Você vai pagar R$ {preco} reais!')
elif pagamento == 2:
    preco = (preco * 95) / 100
    print(f'Você vai pagar R$ {preco} reais!')
elif pagamento == 3:
    print(f'Você vai pagar R$ {preco} reais!')
elif pagamento == 4:
    preco = (preco * 120) / 100
    print(f'Você vai pagar R$ {preco} reais!')

else:
    print('Opção invalida!')