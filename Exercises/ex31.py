# Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preco da passagem, cobrando R$0.50 por KM para viagens ate 200KM e R$0.45 para viagens mais longas.

distancia = float(input('Digite a distancia percorrida: '))
if distancia <= 200:
    preco = distancia * 0.50
    print('Percorrendo {}KM, voce vai ter que pagar R${:.2f}!'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('Percorrendo {}KM, voce vai ter que pagar R${:.2f}!'.format(distancia, preco))
