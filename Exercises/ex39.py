# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
'''- Se ele ainda vai se alistar ao servico militar
- Se eh a hora de alistar
- Se ja passou do tempo do alistamento'''

# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar imediatemente!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce nao precisa se alistar ainda. Ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {} '.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Ja passou da hora de voce se alista ha {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} '.format(ano))