sexo = 'x'

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
print(f'Seu sexo é {sexo}')
