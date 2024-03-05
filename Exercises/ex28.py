#Escreva um programa que faca o computador 'pensar' em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
n = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if n == computador:
    print('Ganhou.')
else:
    print('Perdeu. Eu pensei no numero {}'.format(computador))


