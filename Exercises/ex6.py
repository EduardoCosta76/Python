'Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada'

from math import sqrt
num = float(input('Digite um numero: '))
d = num * 2
t = num * 3
r = sqrt(num)
print('O numero {} tem o seu dobro {}, o seu triplo {} e a sua raiz quadrada {:.2f}!'.format(num, d, t, r))
