import random

#INTRODUÇÃO AO JOGO

print('\33[32m-=\33[m' * 15)
print('\t Oi! Vamos jogar JOKENPÔ?')
print('\33[32m-=\33[m' * 15)

#PLAYER ESCOLHE

esc_pla = str(input('Escolha algum entre Pedra, Papel ou Tesoura:\n')).title()
esc = 0

if esc_pla == 'Pedra':
    esc = 1
elif esc_pla == 'Papel':
    esc = 2
elif esc_pla == 'Tesoura':
    esc = 3

#MAQUINA ESCOLHE

maq = random.randint(1,3)
esc_maq = ' '

if maq == 1:
    esc_maq = 'Pedra'
elif maq == 2:
    esc_maq = 'Papel'
elif maq == 3:
    esc_maq = 'Tesoura'

#Calculo do jogo

if maq == 1 and esc == 3: #PEDRA / TESOURA
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então EU VENCI!')
elif maq == 2 and esc == 1: #PAPEL / PEDRA
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então EU VENCI!')
elif maq == 3 and esc == 2: #TESOURA / PAPEL
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então EU VENCI!')
elif esc == 1 and maq == 3:#PEDRA / TESOURA
    print(f'Eu escolho {esc_maq} e você {esc_pla}, então VOCÊ VENCEU!')
elif esc == 2 and maq == 1:#PAPEL / PEDRA
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então VOCÊ VENCEU!')
elif esc == 3 and maq == 2: #TESOURA / PAPEL
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então VOCÊ VENCEU!')
else:
    print(f'Eu escolhi {esc_maq} e você {esc_pla}, então deu empate!')

