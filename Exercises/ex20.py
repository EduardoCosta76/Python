'O mesmo professor do desafio anterior quer sortear a ordem de apresencacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'

from random import shuffle
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de aprentacao sera: {}!'.format(alunos))

