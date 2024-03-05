# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
'''A media de idade do grupo
Qual eh o nome do homem mais velho
Quantas mulheres tem menos de 20 anos'''

soma = 0
media = 0
maior = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('----{} PESSOA ----'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip()
    soma = soma + idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
     if sexo in 'Ff' and idade < 20:
         totmulher20 += 1
media = soma / 4
print('A media de idade do group eh de {} anos '.format(media))
print('O homem mais velho tem {} anos e se chama {} '.format(maior, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))


