# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome eh {}'.format(nome[0]))
print('Seu ultimo nome eh {}'.format(nome[len(nome)-1]))

