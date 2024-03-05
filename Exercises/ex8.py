'Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros'

num = float(input('Digite um numero: '))
c = num * 100
m = num * 1000
print('O numero {} convertido em centimetros eh de {:.2f}, e em milimetros eh {:.2f}!'.format(num, c, m))
