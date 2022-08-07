palavras = ('jogo', 'lugar', 'paulista', 'francielle',
            'luhan', 'luiza', 'luiz', 'isis', 'safira',
            'loop', 'fernandes', 'casa', 'dinheiro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')