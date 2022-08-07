nome = str(input('Digite o nome da sua cidade: ')).strip()

nome = (nome.title().split())

if nome[0] == 'Santo':
    print('A sua cidade começa com Santo!')
else:
    print('A sua cidade não começa com Santo!')