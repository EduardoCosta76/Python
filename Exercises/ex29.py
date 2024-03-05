# Escreva um programa que leia a velocidade de umn carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

km = float(input('Digite sua velocidade: '))
multa = (km-80) * 7
if km <= 80:
    print('Abaixo do limite, dirija com seguranca!')
else:
    print('A sua velocidade eh de {}KM/s. Voce vai receber uma multa de R${:.2f}!'.format(km, multa))
