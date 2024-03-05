'Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa'

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotonusa vai medir {:.2f}'.format(hi))