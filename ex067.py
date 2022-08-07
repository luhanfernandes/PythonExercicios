num = 1

while num > 0:
    num = int(input('Valor para testar na tabuda: '))

    if num < 0:
        print('Fim do programa!')
        break

    for c in range(1,11):
        print(f'{num} x {c} = {num * c}')
