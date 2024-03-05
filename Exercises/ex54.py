# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantos ja sao maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {} pessoa: '.format(p)))
    idade = atual - pessoa
    if idade <= 21:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade'.format(totmaior, totmenor))