# Crie um programa que faca o computador jogar Jokenpo com voce.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opcoes:
1 - PEDRA
2 - PAPEL
3 - TESOURA''')
jogador = int(input('Qual voce escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
