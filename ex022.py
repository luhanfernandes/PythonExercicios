nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiusculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')


print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras!')

#print('Seu primeiro nome tem {nome.find(" ") letras')

nome = nome.split()
print(f'Seu primeiro nome tem {len(nome[0])} letras!')