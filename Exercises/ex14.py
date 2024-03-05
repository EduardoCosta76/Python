'Escreva um programa que converta um temperatura digitata em graus celsius e converta para F'
c = float(input('Digite a temperatura atual: '))
f = c * 1.8 + 32
print('Convertendo {:.1f}C para F, fica {:.1f}F'.format(c, f))