# Crie um programa que leia um numero inteiro e mostre na tela se ele eh par ou impar.

num = int(input('Digite um numero: '))
res = num % 2
if res == 0:
    print('O numero {} eh par.'.format(num))
else:
    print('O numero {} eh impar.'.format(num))
