import random
from time import sleep

num = random.randint(0,5)
print('-='*30)
print('Estou pensando em um número entre 0 e 5. Você consegue descobrir?')
print('-='*30)

num1 = int(input('Dê seu chute: '))
print('Processando...')
sleep(3)
if num1 == num:
    print('Parabéns, você acertou!')
else:
    print('Por pouco, tente de novo!')
    print(f'O meu numero era: {num}')