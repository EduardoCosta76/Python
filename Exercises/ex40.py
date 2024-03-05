# Crie um programa que leia duas notas de um aluno e calcule a sua media, mostrando uma mensagem no final, de acordo com a media atingida:
'''- Media abaixo de 5.0: REPROVADO
 - Media entre 5.0 e 6.9: RECUPERACAO
 - Media 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('A sua media foi {:.1f}. Abaixo de 5.0: REPROVADO'.format(m))
elif m >= 5 and m <= 6.9:
    print('A sua media foi {:.1f}. Entre 5.0 e 6.9: RECUPERACAO'.format(m))
else:
    print('A sua media foi {:.1f}. Media 7.0 ou superior: APROVADO'.format(m))
