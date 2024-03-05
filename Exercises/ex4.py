'Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.'

n1 = (input('Digite algo: '))
print('O tipo primitivo de {} eh '.format(n1),type(n1))
print('{} eh um numero?'.format(n1), n1.isnumeric())
print('{} eh um texto?'.format(n1), n1.isalpha())
print('{} eh alfabetico? '.format(n1), n1.isalpha())
print('{} esta em maiusculas? '.format(n1), n1.isupper())