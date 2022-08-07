from random import randint

#rever aula 68 - mundo 2

#variaveis
vitoria = 0

while True:

    #jogador
    opjogador = int(input('Diga um valor: '))
    opjogadorparimpar = str(input('Par ou ímpar? [P/I] ')).strip().title()[0]

    #computador
    escolhapc = randint(1,20)
    escolhapcparimpar = ''

    if opjogadorparimpar == 'P':
        escolhapcparimpar = 'I'
    else:
        escolhapcparimpar = 'P'

    #Jogo

    resultnum = (opjogador + escolhapc)
    vencedor = ''

    print(f'Eu escolhi {escolhapc} e você {opjogador}')

    if resultnum % 2 == 0:
        vencedor = 'P'
        print(f'A soma total deu {resultnum}, e ele é Par!')
    else:
        vencedor = 'I'
        print(f'A soma total deu {resultnum}, e ele é impar!')

    if vencedor == opjogadorparimpar:
        print('Parabéns, você venceu!\n')
        vitoria += 1

    else:
        print('Haha, eu venci!')
        print(f'Você conseguiu {vitoria} vitorias consecutivas!\n ')
        break



