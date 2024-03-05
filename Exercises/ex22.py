# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras no total (sem considerar espacos)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome eh {} e ele tem {} letras'.format(separa[0], len(separa[0])))
