# A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''- Ate 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos: JUNIOR
- Ate 25 anos: SENIOR
- Acima: MASTER'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')