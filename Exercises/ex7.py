'Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media'

aluno = input('Digite o seu nome: ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('O aluno {} tirou {} e {} e teve uma media de {:.2f}!'.format(aluno, n1, n2, m))
