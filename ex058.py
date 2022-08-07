from random import randint
from time import sleep

'''num = random.randint(0,5)
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
    print(f'O meu numero era: {num}')'''

numj = -1
nump = randint(0,10)
cont = 0

print('-=' * 30)
print('Estou pensando num número entre 1 e 10, consegue advinhar?')
print('-=' * 30)

while numj != nump:
    if cont == 0:
        numj = int(input('Digite seu palpite: '))
    else:
        numj = int(input('Você errou, mas tente novamente: '))
    cont += 1

if cont == 1:
    print(f'Parabéns, você precisou de apenas {cont} vez para me vencer!')
else:
    print(f'Parabéns, você me venceu, mas precisou de {cont} palpites para isso!')
