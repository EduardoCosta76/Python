# Faca um programa que leia tres numeros e mostre qual eh o maior e qual eh o menor

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('E mais um numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor numero eh {}'.format(menor))
print('O maior numero eh {}'.format(maior))
