# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
'''o PRIMEIRO VALOR EH MAIOR
O SEGUNDO VALOR EH MAIOR
NAO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O numero {} e maior que o {}.'.format(n1, n2))
elif n1 < n2:
    print('O numero {} eh menor que o {}.'.format(n1, n2))
else:
    print('Nao existe valor maior, os dois sao iguais.')